# SOP lifecycle and writing quality

Use this reference when producing an operating document or deciding what evidence is needed before calling it ready.

## Lifecycle

1. **Select:** document work when a written aid reduces a real risk, variation, handoff problem, training burden, or repeated explanation. Record why documentation is useful. No single time or page threshold applies to every team.
2. **Discover:** collect current instructions, interview relevant roles, and inspect representative work or system evidence when available. Compare the written process with work as actually performed; investigate constraints and adaptations without blame. Record date, sample, and gaps. Never present an assumed process as observed fact.
3. **Draft:** use the language and level of detail appropriate to the executor. Give each instruction one primary action and state required inputs, expected result, and verification point.
4. **Review:** ask the process owner, executor, and relevant control or safety owner to check the flow. Resolve disagreements or retain them as open decisions.
5. **Walk through or pilot:** use representative cases, including a foreseeable exception and a failure path. For structured usability testing, prepare scenarios and success criteria before the session; see `assets/sop-usability-test-plan.md`. Observe where users need information that the document omits. A walk-through is evidence of a test, not automatic approval.
6. **Approve and publish:** record the approver role, version, effective date, access location, and change history. Publish only through the organization’s authorized process.
7. **Adopt:** tell affected users what changed, provide role-appropriate training, and make the procedure findable at the point of work where feasible. Put the relevant instruction or checklist near the task when that reduces context switching without hiding required context.
8. **Monitor and improve:** compare process outcome measures with a baseline and gather user feedback. Keep adoption signals (such as completion or help requests) separate from outcome and safety measures; access counts or signed acknowledgments alone do not prove effectiveness. Record changes and rerun affected checks when a system, policy, role, or risk changes.
9. **Review or retire:** set a review date or event trigger. When the process ends or is replaced, mark the old version obsolete, preserve required records, and point users to the successor.

## Writing rules

- Put purpose, scope, owner, and version where users can find them.
- Use active voice and name the role that acts. Begin steps with a precise verb.
- Prefer one action per numbered step. State the required input and expected output when they are not obvious.
- Replace vague words such as “appropriately,” “quickly,” or “as needed” with an observable condition, role, or decision rule.
- Explain acronyms at first use; use the same term for the same object throughout.
- Keep warnings beside the step they affect. Separate required action, rationale, caution, and optional guidance.
- Show branches as explicit conditions and outcomes. State what to do when an input is missing, a tool fails, or a result falls outside the expected range.
- Use a checklist for a short set of critical confirmations; use a procedure when users need the sequence and decision logic. Do not enforce a fixed checklist length.
- Keep steps concise, but preserve the context needed to perform them safely. No universal page or step limit is assumed.

## Organize information for the user’s task

Separate operational instructions from background explanation and exhaustive reference material when combining them makes execution harder. Use stable headings, short labeled sections, tables for decisions, and warnings beside the affected step. Choose a linear numbered list for a simple sequence, a decision table or flow for branching logic, and linked subprocedures when a long document has distinct tasks. Do not split work just to meet a fixed page or step count. Follow the organization’s terminology and accessibility conventions.

For a short, high-consequence checklist, choose deliberately between **read-do** (read each action, then perform it) and **do-confirm** (perform the work, then pause to confirm critical items). Use either only when it fits the task and team; the checklist supports memory and coordination, not expertise or independent judgment. There is no universal item count.

## Validation cases

At minimum, consider:

| Case | Question |
| --- | --- |
| Normal | Can the intended role complete the expected case using only available inputs and permitted tools? |
| Variation | What changes when an input or decision differs? |
| Missing or invalid input | Does the procedure stop safely and identify who resolves the gap? |
| Tool or dependency failure | Is there a retry boundary, recovery path, or escalation owner? |
| Control failure | Does the process prevent proceeding, route to an authorized reviewer, or record an explicit exception? |
| Boundary case | Does a case outside scope get routed without being silently forced through the standard flow? |

Capture the tester’s role, scenarios, observed result, unresolved issue, and review status. If no walk-through was performed, say so.

## Learn from incidents and near misses

When a procedure is connected to an incident or near miss, record the conditions, sequence, impact, signals available at the time, controls that worked or failed, and actions that reduce recurrence. Focus on the system and operating conditions rather than individual blame. Assign each corrective action an owner and a way to verify completion; update the procedure only when it is the right control.

## Governance fields

Use only fields that help the organization control the document. Common fields include title, owner role, approver role, version, status, effective date, review date or trigger, scope, source documents, and change history. Define status labels locally; for example, “draft,” “reviewed,” “pilot,” and “approved” must not be treated as interchangeable.

## Versioned and living documentation

Where the team can support it, store procedures as versioned text, review changes with the same rigor as the process they govern, and run spelling, link, or structure checks automatically. This docs-as-code approach can improve traceability, but it is optional; use the organization’s approved document system when it better supports access, approval, records, or retention requirements. Keep generated documents synchronized with the process and system they describe, and identify who updates each dependency.

For technical operations, use a **runbook** for a known operation or failure with concrete steps and checks. Use a **playbook** when the response depends on scenario, evidence, or choices. Give incident procedures explicit severity/ownership rules, communication roles, decision points, recovery checks, and post-incident learning steps. Follow the organization’s approved incident and record-handling policies.
