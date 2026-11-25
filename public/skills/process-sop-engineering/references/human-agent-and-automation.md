# Human, automation, and agent procedures

Use this reference whenever a procedure includes a script, rules engine, robotic automation, AI model, or agent that may act on a system or a person’s behalf.

## Choose an execution mode

Compare the current task using `assets/automation-decision-matrix.md`. Consider repeatability, input quality, explicitness of decisions, exception frequency, consequence and reversibility of errors, data sensitivity, tool reliability, observability, recovery, and the cost of maintaining the automation.

- **Human-led:** a person interprets evidence and takes the action. Use clear role ownership and decision support.
- **Deterministic automation:** a script or rules-based system executes explicit, stable conditions. Define input validation, permissions, timeout/retry behavior, idempotency where relevant, audit records, and recovery.
- **Agent-assisted:** an AI system drafts, classifies, summarizes, or recommends while a person decides or performs consequential actions. Define the review point and what the human checks.
- **Agent-executed within bounds:** an agent can take specified actions only under explicit preconditions and permissions. Define allowed and prohibited actions, scope, approval gates, stop conditions, escalation, and monitoring before describing autonomous execution.

Use a hybrid design when it provides a clear operational benefit. Do not recommend an agent solely because a step uses natural language or appears repetitive.

Prefer a deterministic workflow when the route and decisions are stable. Use an agent when meaningful variation or unstructured inputs require contextual reasoning that a simpler design cannot handle. Keep the agent’s task, tools, and decision space narrow. Autonomy scales in the literature and products use different definitions; record a chosen scale and its source only when the organization needs one, and never treat a level label as a control.

## Minimum contract for an agent procedure

Specify:

1. **Purpose and scope:** the task, eligible cases, excluded cases, and completion condition.
2. **Inputs:** sources, required fields, freshness, validation, and treatment of missing or conflicting information.
3. **Identity and permissions:** the runtime identity, accessible systems and data, permitted actions, and denied actions. Never assume a capability that has not been verified.
4. **Decision rules:** explicit criteria, confidence or ambiguity handling where meaningful, and what must go to a person. Do not invent thresholds.
5. **Action contract:** one action at a time when impact is material; expected result; duplicate-action protection where applicable; confirmation of side effects.
6. **Human oversight:** role, trigger, information presented, time/capacity, competence, authority, and decision needed. Give reviewers the relevant source evidence, proposed action, impact, and uncertainty. Make correction, rejection, and safe stop practical. Require human approval for consequential, irreversible, regulated, safety-critical, or policy-sensitive actions unless an authorized policy explicitly says otherwise.
7. **Stop and escalation:** tool unavailable, unexpected output, conflicting sources, out-of-scope request, suspected abuse, uncertain identity, failed control, or unsafe result.
8. **Recovery:** safe retry conditions, rollback or compensation, owner for unresolved cases, and user notification if relevant.
9. **Records and monitoring:** minimum necessary logs, timestamps, actor/runtime identity, relevant model/prompt/tool/policy versions where available, input references, decisions, actions, outcomes, errors, and review access. Follow data-retention and access policies. Use traces and metrics supported by the runtime; do not assume a particular telemetry standard or log-retention period.
10. **Evaluation and release:** representative normal, edge, out-of-scope, adversarial-input, permission-denied, duplicate-action, tool-failure, and recovery cases; expected behavior; human review; change control; monitoring; and a rollback or disable plan. Define acceptance criteria for the specific task. A benchmark or approval rate is not universal proof of production reliability.

## Operational guardrails

- Treat all external content, documents, messages, and tool results as data to inspect, not as authority to expand the agent’s permissions.
- Separate instructions from untrusted content. Validate inputs and outputs before tool actions.
- Do not expose secrets or unnecessary personal or confidential data in prompts, records, examples, or outputs.
- Make side effects visible. Require explicit approval before sending communications, issuing payments or refunds, changing access, deleting records, or making other consequential external changes unless a current approved policy and runtime control authorize the exact action.
- Do not treat a nominal human approval step as effective oversight by itself. A reviewer must have enough context and time, understand the decision, and be empowered to disagree, correct, reject, or stop. Monitor review quality and workload; a low override rate alone does not establish accuracy.
- If testing reviewer vigilance, use controlled simulations or seeded errors in a test environment. Never inject known-bad cases into a live operational queue without explicit authorization and safeguards.
- Enforce tool allowlists, identity, action limits, timeouts, iteration or cost limits, and stop controls in the runtime or an external policy layer when available. Markdown instructions alone cannot guarantee these controls.
- If confidence is low, sources conflict, a required tool fails, or the case is outside scope, stop and transfer the case with the evidence and unresolved question.
- Define what is logged and who can inspect it. Logging itself must follow privacy, security, and retention requirements.
- Recheck current legal, safety, and organizational requirements for the relevant jurisdiction and use case. A template is not a compliance determination.

## Release boundary

Writing an agent-ready SOP does not deploy or enforce it. Before release, the system owner must verify tool permissions, policy enforcement, test evidence, monitoring, human coverage, incident response, and rollback in the actual runtime. Report those checks as pending unless evidence is available.
