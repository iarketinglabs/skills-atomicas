# Template de `architecture.md`

Fonte canônica única deste template — referenciada (não copiada) por `../references/architecture-md.md` e `../references/behavior-isolation.md`. Esqueleto pronto para adaptar como a constituição permanente de um repositório — nunca escrito por um agente, sempre redigido e mantido por um engenheiro sênior humano (ver `../references/architecture-md.md` para o porquê).

```markdown
# CONSTITUTIONAL ARCHITECTURE & RULES OF ENGAGEMENT

You are the Lead Software Architect of this repository. Your primary directive
is to enforce correct, modular, secure, and maintainable implementations.
Every code modification must adhere strictly to the rules defined in this document.

## 1. REPOSITORY TOPOLOGY & BEHAVIOR ISOLATION
All features must be structured by isolated behaviors, ensuring no single file
becomes a monolithic block.
- `/src/pages/`: Contains page directories.
- Within each page folder, there must be a `/components` subfolder and behavioral
  folders representing isolated actions (e.g., `/auth`, `/billing`).
- An agent operating on a feature inside `/billing` is strictly forbidden from
  inspecting, modifying, or reading files inside `/auth` unless explicit
  authorization is granted in the plan. This prevents the "Blanket Effect"
  (breaking feature A while fixing feature B).

## 2. SECURITY POLICY: "THIN CLIENT, FAT SERVER"
We enforce strict data protection and separation of concerns.
- **Client-Side (Front-End) Constraints:** the front-end must remain a visual
  presentation layer only.
  - NEVER write business logic, rate limits, or user role validation inside
    front-end components.
  - NEVER expose secret keys in front-end files.
  - The client is a Thin Client; it only captures user intent and forwards it
    to the server.
- **Server-Side (Back-End) Enforcement:**
  - All critical business logic, quota calculations, and database mutations
    must execute securely in the back-end.
  - Every data table must have row-level access control enabled.
  - Front-end API calls must strictly use the public/anonymous credential,
    which automatically respects those access-control policies.

## 3. FEEDBACK LOOPS & COMPILATION SAFETY (ANTI-GHOST REGULATION)
To avoid endless debugging loops and context bloat:
- NEVER run background dev-server commands synchronously in terminal tools.
- To verify compilation and code health, run exactly the project's static
  type-check command.
- Clean any syntax, linter, or type errors locally in your workspace before
  creating a pull request. Do not leave "ghost" errors in the repository.

## 4. EXPERTISE DIRECTORIES (REUSABILITY GUIDELINES)
- Before creating a utility function or script from scratch, inspect the
  shared-packages folder.
- Ensure all business-related functions use identical shared packages to
  maintain a single source of truth across every channel (web, mobile, CLI).
- Keep the test suite read-only. You are strictly forbidden from modifying or
  commenting out existing assertions in the test files. To succeed, make your
  implementation pass the tests — do not change the tests to hide failures.
```

## Como adaptar

Substitua os caminhos de exemplo (`/src/pages/`, `/billing`, `/auth`) pela topologia real do seu repositório. As quatro seções (topologia + isolamento, política de segurança, segurança de compilação, diretórios de expertise) são o mínimo — adicione seções específicas do seu domínio, mas nunca delegue a escrita ou a manutenção deste arquivo a um agente.
