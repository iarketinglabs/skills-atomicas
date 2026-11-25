#!/usr/bin/env node
// Instantiate Kanban Dashboard — copia a base genérica de dashboard kanban
// (assets/kanban-dashboard/) para dentro do projeto do cliente.
//
// 100% agnóstico a cliente/stack: não lê nem escreve nada fora de
// assets/kanban-dashboard/ (origem) e da pasta --target (destino). Não
// depende de nenhum MCP, credencial ou dependência externa (só node:fs/node:path).
//
// Idempotente: nunca sobrescreve um arquivo já existente no destino, só cria
// o que falta — pode ser rodado de novo com segurança.
//
// Uso:
//   node instantiate-kanban-dashboard.mjs --target /caminho/do/projeto/.../dashboard
//
// Depois de instanciado, o dashboard roda a partir da pasta destino:
//   cd /caminho/do/projeto/.../dashboard
//   node build-data.mjs && node server.mjs

import { readdirSync, statSync, mkdirSync, copyFileSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SOURCE_DIR = join(__dirname, "..", "assets", "kanban-dashboard");

function parseArgs(argv) {
  const args = { target: null };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--target" && argv[i + 1]) {
      args.target = argv[i + 1];
      i++;
    }
  }
  return args;
}

function listFilesRecursive(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      out.push(...listFilesRecursive(full));
    } else {
      out.push(full);
    }
  }
  return out;
}

function main() {
  const { target } = parseArgs(process.argv.slice(2));

  if (!target) {
    console.error("Uso: node instantiate-kanban-dashboard.mjs --target <pasta-de-destino-no-projeto>");
    process.exit(1);
  }

  if (!existsSync(SOURCE_DIR)) {
    console.error(`Pasta de origem não encontrada: ${SOURCE_DIR}`);
    process.exit(1);
  }

  const targetDir = resolve(target);
  mkdirSync(targetDir, { recursive: true });

  const sourceFiles = listFilesRecursive(SOURCE_DIR);
  const created = [];
  const skipped = [];

  for (const sourceFile of sourceFiles) {
    const relative = sourceFile.slice(SOURCE_DIR.length + 1);
    const destFile = join(targetDir, relative);
    mkdirSync(dirname(destFile), { recursive: true });

    if (existsSync(destFile)) {
      skipped.push(relative);
      continue;
    }
    copyFileSync(sourceFile, destFile);
    created.push(relative);
  }

  console.log(`Dashboard instanciado em: ${targetDir}`);
  console.log(`Criados: ${created.length}`);
  for (const f of created) console.log(`  + ${f}`);
  if (skipped.length) {
    console.log(`Já existiam (não sobrescritos): ${skipped.length}`);
    for (const f of skipped) console.log(`  = ${f}`);
  }
  console.log("");
  console.log("Próximos passos:");
  console.log(`  cd ${targetDir}`);
  console.log("  node build-data.mjs   # lê os .md do caderno de testes e gera data.json");
  console.log("  node server.mjs        # sobe o dashboard em http://127.0.0.1:4545");
}

main();
