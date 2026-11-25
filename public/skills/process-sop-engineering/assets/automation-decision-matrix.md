# Execution-mode decision matrix

Use this matrix to structure a discussion, not as an automatic score or substitute for policy approval. Add local criteria and thresholds only when an authorized owner provides them.

| Factor | Human-led is a stronger fit when… | Deterministic automation is a stronger fit when… | Agent assistance may fit when… | Bounded agent execution needs… |
| --- | --- | --- | --- | --- |
| Process stability | The case depends on context and judgment | Steps and decision rules are explicit and stable | Language-heavy work benefits from a draft, summary, or recommendation | Stable eligibility, actions, and boundaries are approved |
| Input quality | Evidence needs interpretation or relationship context | Inputs are structured and validated | Documents or text need classification or synthesis | Source authority, freshness, validation, and conflict handling are defined |
| Variation | Cases vary widely and experts adapt | Variants can be expressed as clear rules | The system can help organize options for human review | Exceptions are bounded and transfer safely to a human |
| Error impact | Consequences need accountable human judgment | Errors are low impact or well-contained and recoverable | A person can check recommendations before action | Explicit permission, approval, stop, audit, and recovery controls exist |
| Reversibility | Action is consequential or difficult to undo | Actions are reversible, idempotent, or compensable | Output is advisory and no side effect occurs without review | Side effects and rollback/compensation are tested |
| Data and access | Sensitive data or context requires restricted handling | Least-privilege access and deterministic validation are available | Data can be minimized and checked before use | Runtime identity, least privilege, retention, and audit access are verified |
| Human oversight capacity | A qualified role can make the decision with the needed context | A person owns exceptions or review when rules do not cover a case | Reviewer has the evidence, time, skill, and authority to correct the recommendation | Review volume is bounded; reject/correct/stop paths work and reviewer capacity is monitored |
| Monitoring and recovery | Work is infrequent or exceptional; a responsible expert is available | Events and failures can be detected and routed | A reviewer can validate output and correct it | Coverage, alerts, error budget/limits, fallback, and disable path are owned |

## Decision record

- **Selected mode:**
- **Why it fits:**
- **What remains human-owned:**
- **Actions that are prohibited or require approval:**
- **Evidence or test still needed:**
- **Process, system, and control owner roles:**
- **Review trigger:**

Treat uncertainty, high impact, weak source quality, missing policy, low reversibility, or untested permissions as reasons to reduce autonomy until the responsible owner resolves them.
