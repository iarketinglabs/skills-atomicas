// Lê os arquivos .md de um caderno de testes (template de caso de teste em
// references/checklists-and-templates.md da skill testes-qa), extrai os casos
// de teste e gera data.json para o dashboard kanban. Sem dependências externas
// — só node:fs/node:path. 100% agnóstico a projeto/cliente: nenhum nome de
// arquivo é assumido, a descoberta é por conteúdo.
//
// Uso (a partir da pasta onde este arquivo foi copiado, ver README.md):
//   node build-data.mjs                  # escaneia a pasta-mãe (padrão)
//   node build-data.mjs --source ../casos # escaneia uma pasta específica

import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { dirname, join, extname, basename } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));

// Ordem lógica de execução (opcional, agnóstica a projeto): se existir um
// sequence.json nesta mesma pasta, os cards seguem essa ordem em vez de
// ordem alfabética de TEST_ID — ver references/kanban-dashboard.md para o
// formato ({ "phases": [ { "label": "...", "ids": ["X-01", ...] }, ... ] }).
// Casos não listados caem no fim, em ordem alfabética entre si.
function loadSequence() {
  const path = join(__dirname, "sequence.json");
  if (!existsSync(path)) return { orderById: new Map(), phaseById: new Map() };
  const data = JSON.parse(readFileSync(path, "utf8"));
  const orderById = new Map();
  const phaseById = new Map();
  let i = 0;
  (data.phases || []).forEach((phase, phaseIndex) => {
    for (const id of phase.ids) {
      orderById.set(id, i++);
      phaseById.set(id, { index: phaseIndex, label: phase.label });
    }
  });
  return { orderById, phaseById };
}

function parseArgs(argv) {
  const args = { source: null };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--source" && argv[i + 1]) {
      args.source = argv[i + 1];
      i++;
    }
  }
  return args;
}

const cliArgs = parseArgs(process.argv.slice(2));
const sourceDir = cliArgs.source ? join(process.cwd(), cliArgs.source) : join(__dirname, "..");

// Campos do template canônico de caso de teste (references/checklists-and-templates.md),
// mais as variantes simplificadas mais comuns que um projeto pode adotar. Um caderno
// não precisa preencher todos — o que faltar simplesmente não aparece no painel lateral.
// Ordem não importa (ver FIELD_LINE_RE).
const FIELD_KEY = {
  TEST_ID: "id",
  TÍTULO: "titulo",
  OWNER: "owner",
  TEST_BASIS: "testBasis",
  RISCO: "risco",
  "OBJETO E FRONTEIRAS": "objetoFronteiras",
  NÍVEL: "nivel",
  TÉCNICA: "tecnica",
  "PRECONDIÇÕES E DADOS": "precondicoes",
  PRECONDIÇÕES: "precondicoes", // variante simplificada
  ESTADO_INICIAL: "estadoInicial",
  "PASSOS/AÇÃO": "passos",
  PASSOS: "passos", // variante simplificada
  ORÁCULO: "oraculo",
  AMBIENTE: "ambiente",
  EVIDÊNCIA: "evidencia",
  RESULTADO: "resultado",
  "FALHA/CAUSA/OWNER": "falhaCausaOwner",
  "VERSÕES E ÚLTIMA EXECUÇÃO": "versoes",
  VERSÕES: "versoes", // variante simplificada
};

const FIELD_NAMES = Object.keys(FIELD_KEY);
const FIELD_LINE_RE = new RegExp(`^(${FIELD_NAMES.join("|")}):\\s?(.*)$`);
const TEST_ID_BLOCK_RE = /```text\n([\s\S]*?)```/g;

function extractTextBlocks(markdown) {
  const blocks = [];
  let m;
  // regex com estado (lastIndex) — sempre usar uma instância nova por arquivo
  const re = new RegExp(TEST_ID_BLOCK_RE);
  while ((m = re.exec(markdown))) {
    blocks.push(m[1]);
  }
  return blocks;
}

function parseEntries(blockText) {
  const lines = blockText.split("\n");
  const entries = [];
  let current = null;
  let currentFieldKey = null;
  let currentFieldLines = [];

  function flushField() {
    if (current && currentFieldKey) {
      current[currentFieldKey] = currentFieldLines.join("\n").trim();
    }
    currentFieldKey = null;
    currentFieldLines = [];
  }

  function flushEntry() {
    flushField();
    if (current && current.id) {
      entries.push(current);
    }
    current = null;
  }

  for (const rawLine of lines) {
    const line = rawLine.replace(/\r$/, "");
    const fieldMatch = line.match(FIELD_LINE_RE);
    if (fieldMatch) {
      const label = fieldMatch[1];
      const rest = fieldMatch[2] ?? "";
      if (label === "TEST_ID") {
        flushEntry();
        current = {};
      }
      flushField();
      currentFieldKey = FIELD_KEY[label];
      currentFieldLines = [rest];
    } else if (current) {
      currentFieldLines.push(line);
    }
  }
  flushEntry();
  return entries;
}

// Deriva um rótulo de área legível a partir do nome do arquivo, sem nenhum
// mapa manual por projeto — ex.: "02-fluxo-de-pagamento.md" -> "Fluxo De Pagamento".
const LOWERCASE_CONNECTORS = new Set(["e", "de", "da", "do", "das", "dos", "a", "o", "em", "com", "para"]);

function humanizeFilename(filename) {
  let name = basename(filename, extname(filename));
  name = name.replace(/^\d+[-_]+/, ""); // remove prefixo numérico de ordenação, se houver
  const words = name.split(/[-_]+/).filter(Boolean);
  return words
    .map((w, i) => {
      const lower = w.toLowerCase();
      if (i > 0 && LOWERCASE_CONNECTORS.has(lower)) return lower;
      return lower.charAt(0).toUpperCase() + lower.slice(1);
    })
    .join(" ");
}

// Divide o texto de RESULTADO em cláusulas de topo separadas por " / ",
// ignorando qualquer "/" que apareça dentro de parênteses (ex.: caminho de
// arquivo numa nota entre parênteses) — só o "/" usado como separador de
// resultado composto ("pass (...) / a executar (...)") conta. Um caso pode
// ter resultado composto quando cobre mais de um nível (ex.: componente já
// automatizado + sistema ainda manual) — ver references/kanban-dashboard.md.
function splitTopLevelClauses(resultado) {
  const clauses = [];
  let depth = 0;
  let current = "";
  const text = resultado || "";
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "(") depth++;
    if (ch === ")") depth = Math.max(0, depth - 1);
    if (depth === 0 && text.slice(i, i + 3) === " / ") {
      clauses.push(current);
      current = "";
      i += 2;
      continue;
    }
    current += ch;
  }
  clauses.push(current);
  return clauses;
}

function clauseStatus(clause) {
  const head = clause.split(/[\n(]/)[0].trim().toLowerCase();
  if (head.startsWith("pass")) return "aprovado";
  if (head.startsWith("blocked")) return "bloqueado";
  if (head.startsWith("fail")) return "reprovado";
  if (head.startsWith("inconclusive") || head.startsWith("inconclusivo")) return "inconclusivo";
  if (head.startsWith("a executar")) return "a_executar";
  return "a_executar";
}

// Prioridade de qual cláusula "vence" quando o RESULTADO é composto. Trabalho
// ainda pendente (a_executar/bloqueado) sempre vence — o card só deve
// aparecer como concluído (aprovado/reprovado) quando TODAS as partes já
// rodaram, ajuste as palavras-chave se seu caderno usar outro vocabulário.
const STATUS_PRIORITY = ["a_executar", "bloqueado", "inconclusivo", "reprovado", "aprovado"];

function normalizeStatus(resultado) {
  const statuses = splitTopLevelClauses(resultado).map(clauseStatus);
  for (const candidate of STATUS_PRIORITY) {
    if (statuses.includes(candidate)) return candidate;
  }
  return "a_executar"; // inclui "a executar", vazio, ou qualquer outro texto — estado padrão de backlog
}

// Classifica o "tipo de execução" a partir do texto livre do campo NÍVEL, para
// alimentar o filtro "Execução" do dashboard — não é um campo do template
// original, é uma heurística sobre o texto (ajuste as palavras-chave abaixo
// se o seu caderno usar outra terminologia).
function classifyExecutionKind(nivel) {
  const n = (nivel || "").toLowerCase();
  if (n.includes("automatizado")) return "automatizado";
  if (n.includes("revisão de código") || n.includes("revisao de codigo")) return "revisao_codigo";
  if (n.includes("manual")) return "manual";
  return "outro";
}

function main() {
  let files;
  try {
    files = readdirSync(sourceDir).filter((f) => {
      if (extname(f).toLowerCase() !== ".md") return false;
      return statSync(join(sourceDir, f)).isFile();
    });
  } catch (err) {
    console.error(`Não foi possível ler a pasta ${sourceDir}: ${err.message}`);
    process.exit(1);
  }

  const { orderById, phaseById } = loadSequence();
  const allEntries = [];
  const filesWithCases = [];

  for (const file of files) {
    const content = readFileSync(join(sourceDir, file), "utf8");
    const blocks = extractTextBlocks(content);
    let countInFile = 0;

    for (const block of blocks) {
      const entries = parseEntries(block);
      for (const entry of entries) {
        countInFile++;
        const phase = phaseById.get(entry.id) || null;
        allEntries.push({
          id: entry.id,
          titulo: entry.titulo || "",
          owner: entry.owner || "",
          testBasis: entry.testBasis || "",
          risco: entry.risco || "",
          objetoFronteiras: entry.objetoFronteiras || "",
          nivel: entry.nivel || "",
          tecnica: entry.tecnica || "",
          precondicoes: entry.precondicoes || "",
          estadoInicial: entry.estadoInicial || "",
          passos: entry.passos || "",
          oraculo: entry.oraculo || "",
          ambiente: entry.ambiente || "",
          evidencia: entry.evidencia || "",
          resultado: entry.resultado || "",
          falhaCausaOwner: entry.falhaCausaOwner || "",
          versoes: entry.versoes || "",
          status: normalizeStatus(entry.resultado || ""),
          executionKind: classifyExecutionKind(entry.nivel || ""),
          file,
          area: humanizeFilename(file),
          sequenceOrder: orderById.has(entry.id) ? orderById.get(entry.id) : Infinity,
          phaseIndex: phase ? phase.index : Infinity,
          phaseLabel: phase ? phase.label : "",
        });
      }
    }

    if (countInFile > 0) filesWithCases.push(file);
  }

  // Ordem lógica (sequence.json) primeiro, se existir; qualquer caso não
  // listado (ou se o arquivo não existir) cai em ordem alfabética de ID.
  allEntries.sort((a, b) => a.sequenceOrder - b.sequenceOrder || a.id.localeCompare(b.id));

  const outPath = join(__dirname, "data.json");
  writeFileSync(
    outPath,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        sourceDir,
        sourceFiles: filesWithCases,
        total: allEntries.length,
        tests: allEntries,
      },
      null,
      2
    ),
    "utf8"
  );

  console.log(`Pasta escaneada: ${sourceDir}`);
  console.log(`Arquivos .md com casos de teste: ${filesWithCases.length} de ${files.length} encontrados.`);
  console.log(`OK — ${allEntries.length} casos de teste lidos.`);
  console.log(`Gravado em ${outPath}`);

  if (allEntries.length === 0) {
    console.log(
      "Nenhum caso encontrado — confirme que os arquivos usam blocos ```text com entradas TEST_ID: (ver references/checklists-and-templates.md e references/kanban-dashboard.md)."
    );
  }
}

main();
