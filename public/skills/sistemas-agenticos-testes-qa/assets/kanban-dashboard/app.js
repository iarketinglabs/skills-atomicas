// Dashboard kanban do caderno de testes — sem framework, sem build step.
// Estado de coluna movido manualmente é persistido em localStorage
// (o data.json gerado pelo build-data.mjs nunca é reescrito por esta página).

const STORAGE_KEY = "kanban-dashboard-overrides-v1";

const COLUMNS = [
  { status: "a_executar", label: "A Executar", color: "var(--col-a-executar)" },
  { status: "bloqueado", label: "Bloqueado", color: "var(--col-bloqueado)" },
  { status: "aprovado", label: "Aprovado", color: "var(--col-aprovado)" },
  { status: "reprovado", label: "Reprovado", color: "var(--col-reprovado)" },
  { status: "inconclusivo", label: "Inconclusivo", color: "var(--col-inconclusivo)" },
];

const COLUMN_BY_STATUS = Object.fromEntries(COLUMNS.map((c) => [c.status, c]));

const EXECUTION_KIND_LABEL = {
  manual: "Manual",
  automatizado: "Automatizado",
  revisao_codigo: "Revisão de código",
  outro: "Outro",
};

const state = {
  tests: [],
  overrides: loadOverrides(),
  search: "",
  areaFilter: "",
  executionFilter: "",
};

function loadOverrides() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveOverrides() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.overrides));
}

function effectiveStatus(test) {
  return state.overrides[test.id] || test.status;
}

function extractPriority(risco) {
  const m = /prioridade\s+(alta|média|media|baixa)/i.exec(risco || "");
  if (!m) return null;
  const v = m[1].toLowerCase().replace("media", "média");
  return v;
}

function priorityColor(priority) {
  if (priority === "alta") return "var(--pri-alta)";
  if (priority === "média") return "var(--pri-media)";
  if (priority === "baixa") return "var(--pri-baixa)";
  return "var(--pri-none)";
}

function matchesFilters(test) {
  const q = state.search.trim().toLowerCase();
  if (q) {
    const hay = (test.id + " " + test.titulo).toLowerCase();
    if (!hay.includes(q)) return false;
  }
  if (state.areaFilter && test.area !== state.areaFilter) return false;
  if (state.executionFilter && test.executionKind !== state.executionFilter) return false;
  return true;
}

function render() {
  const board = document.getElementById("board");
  board.innerHTML = "";

  for (const col of COLUMNS) {
    const testsInColumn = state.tests.filter(
      (t) => effectiveStatus(t) === col.status && matchesFilters(t)
    );

    const columnEl = document.createElement("section");
    columnEl.className = "column";
    columnEl.dataset.status = col.status;
    columnEl.setAttribute("aria-label", `Coluna ${col.label}`);

    const header = document.createElement("div");
    header.className = "column-header";
    header.innerHTML = `
      <span class="column-dot" style="background:${col.color}"></span>
      <span class="column-title">${col.label}</span>
      <span class="column-count">${testsInColumn.length}</span>
    `;
    columnEl.appendChild(header);

    const list = document.createElement("div");
    list.className = "column-list";

    if (testsInColumn.length === 0) {
      const empty = document.createElement("div");
      empty.className = "column-empty";
      empty.textContent = "Nenhum card aqui";
      list.appendChild(empty);
    } else {
      let lastPhase = null;
      for (const test of testsInColumn) {
        if (test.phaseLabel && test.phaseLabel !== lastPhase) {
          list.appendChild(renderPhaseDivider(test.phaseLabel));
          lastPhase = test.phaseLabel;
        }
        list.appendChild(renderCard(test));
      }
    }

    columnEl.appendChild(list);
    attachDropZone(columnEl, list);
    board.appendChild(columnEl);
  }
}

function renderPhaseDivider(label) {
  const el = document.createElement("div");
  el.className = "phase-divider";
  el.textContent = label;
  return el;
}

function renderCard(test) {
  const tpl = document.getElementById("card-template");
  const node = tpl.content.firstElementChild.cloneNode(true);

  node.dataset.id = test.id;
  node.querySelector(".card-id").textContent = test.id;
  node.querySelector(".card-title").textContent = test.titulo;

  const priority = extractPriority(test.risco);
  const priorityEl = node.querySelector(".card-priority");
  priorityEl.style.background = priorityColor(priority);
  priorityEl.title = priority ? `Prioridade ${priority}` : "Prioridade não informada";

  node.querySelector(".tag-area").textContent = test.area;
  const nivelTag = node.querySelector(".tag-nivel");
  nivelTag.textContent = shortNivel(test.nivel);
  nivelTag.title = test.nivel;

  node.addEventListener("dragstart", (e) => {
    e.dataTransfer.setData("text/plain", test.id);
    e.dataTransfer.effectAllowed = "move";
    node.classList.add("dragging");
  });
  node.addEventListener("dragend", () => node.classList.remove("dragging"));

  node.addEventListener("click", () => openPanel(test));
  node.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      openPanel(test);
    }
  });

  return node;
}

function shortNivel(nivel) {
  if (!nivel) return "—";
  const first = nivel.split(/[\s(]/)[0];
  return first.charAt(0).toUpperCase() + first.slice(1);
}

function attachDropZone(columnEl, listEl) {
  columnEl.addEventListener("dragover", (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
    columnEl.classList.add("drag-over");
  });
  columnEl.addEventListener("dragleave", (e) => {
    if (!columnEl.contains(e.relatedTarget)) {
      columnEl.classList.remove("drag-over");
    }
  });
  columnEl.addEventListener("drop", (e) => {
    e.preventDefault();
    columnEl.classList.remove("drag-over");
    const id = e.dataTransfer.getData("text/plain");
    if (!id) return;
    const test = state.tests.find((t) => t.id === id);
    if (!test) return;
    const newStatus = columnEl.dataset.status;
    if (newStatus === test.status) {
      delete state.overrides[id];
    } else {
      state.overrides[id] = newStatus;
    }
    saveOverrides();
    render();
  });
}

// ---------- Painel lateral ----------

function statusMeta(status) {
  return COLUMN_BY_STATUS[status] || COLUMN_BY_STATUS.a_executar;
}

function openPanel(test) {
  const panel = document.getElementById("panel");
  const overlay = document.getElementById("overlay");
  const content = document.getElementById("panel-content");

  const current = effectiveStatus(test);
  const currentMeta = statusMeta(current);
  const documented = statusMeta(test.status);
  const wasMoved = state.overrides[test.id] && state.overrides[test.id] !== test.status;

  content.innerHTML = `
    <span class="panel-eyebrow">${escapeHtml(test.id)}</span>
    <h2 class="panel-title">${escapeHtml(test.titulo)}</h2>
    <div class="panel-status-row">
      <span class="status-pill"><span class="dot" style="background:${currentMeta.color}"></span>${currentMeta.label} (atual no quadro)</span>
      ${wasMoved ? `<span class="status-pill"><span class="dot" style="background:${documented.color}"></span>${documented.label} (documentado no caderno)</span>` : ""}
    </div>
    ${section("Fase da jornada de teste", escapeHtml(test.phaseLabel))}
    ${section("Área", escapeHtml(test.area))}
    ${section("Owner", escapeHtml(test.owner))}
    ${section("Nível", escapeHtml(test.nivel))}
    ${section("Técnica", escapeHtml(test.tecnica))}
    ${section("Test basis", escapeHtml(test.testBasis))}
    ${section("Risco", escapeHtml(test.risco))}
    ${section("Objeto e fronteiras", escapeHtml(test.objetoFronteiras))}
    ${section("Pré-condições e dados", escapeHtml(test.precondicoes))}
    ${section("Estado inicial", escapeHtml(test.estadoInicial))}
    ${section("Passos/ação", escapeHtml(test.passos), true)}
    ${section("Oráculo", escapeHtml(test.oraculo))}
    ${section("Ambiente", escapeHtml(test.ambiente))}
    ${section("Evidência", escapeHtml(test.evidencia))}
    ${section("Resultado documentado no caderno", escapeHtml(test.resultado))}
    ${section("Falha / Causa / Owner", escapeHtml(test.falhaCausaOwner))}
    ${section("Versões e última execução", escapeHtml(test.versoes))}
    <div class="panel-footer">
      Fonte: <code>${escapeHtml(test.file)}</code> (na pasta do caderno de testes)<br/>
      Mover este card no quadro grava só neste navegador (localStorage) — não altera o arquivo .md de origem.
    </div>
  `;

  panel.hidden = false;
  overlay.hidden = false;
  requestAnimationFrame(() => panel.classList.add("open"));
  panel.setAttribute("aria-hidden", "false");
}

function section(title, value, monoMultiline = false) {
  if (!value) return "";
  const cls = monoMultiline ? "mono" : "";
  const tag = monoMultiline ? "pre" : "p";
  return `<div class="panel-section"><h4>${escapeHtml(title)}</h4><${tag} class="${cls}">${value}</${tag}></div>`;
}

function closePanel() {
  const panel = document.getElementById("panel");
  const overlay = document.getElementById("overlay");
  panel.classList.remove("open");
  panel.setAttribute("aria-hidden", "true");
  overlay.hidden = true;
  setTimeout(() => {
    if (!panel.classList.contains("open")) panel.hidden = true;
  }, 220);
}

function escapeHtml(str) {
  return String(str || "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  }[c]));
}

// ---------- Toolbar ----------

function setupToolbar() {
  const search = document.getElementById("search");
  search.addEventListener("input", () => {
    state.search = search.value;
    render();
  });

  const areaFilter = document.getElementById("area-filter");
  const areas = [...new Set(state.tests.map((t) => t.area))].sort();
  for (const area of areas) {
    const opt = document.createElement("option");
    opt.value = area;
    opt.textContent = area;
    areaFilter.appendChild(opt);
  }
  areaFilter.addEventListener("change", () => {
    state.areaFilter = areaFilter.value;
    render();
  });

  const executionFilter = document.getElementById("execution-filter");
  if (executionFilter) {
    executionFilter.addEventListener("change", () => {
      state.executionFilter = executionFilter.value;
      render();
    });
  }

  document.getElementById("reset-btn").addEventListener("click", () => {
    if (confirm("Descartar todas as movimentações manuais e voltar ao status documentado no caderno?")) {
      state.overrides = {};
      saveOverrides();
      render();
    }
  });

  document.getElementById("export-btn").addEventListener("click", exportState);

  document.getElementById("panel-close").addEventListener("click", closePanel);
  document.getElementById("overlay").addEventListener("click", closePanel);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closePanel();
  });
}

function exportState() {
  const snapshot = state.tests.map((t) => ({
    id: t.id,
    titulo: t.titulo,
    status_documentado: t.status,
    status_atual: effectiveStatus(t),
    area: t.area,
    execucao: t.executionKind,
  }));
  const blob = new Blob([JSON.stringify(snapshot, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `kanban-dashboard-estado-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
}

// ---------- Boot ----------

async function boot() {
  const res = await fetch("data.json");
  const data = await res.json();
  state.tests = data.tests;
  setupToolbar();
  render();
}

boot().catch((err) => {
  document.getElementById("board").innerHTML =
    `<p style="padding:24px;color:#c0392b">Falha ao carregar data.json — rode <code>node build-data.mjs</code> nesta pasta e recarregue. (${err.message})</p>`;
});
