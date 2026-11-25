# Human factors, reliability, and usability

Use this reference when written instructions interact with real-world variation, interruption, time pressure, coordination, or safety and quality risks.

## Compare prescribed work with actual work

Treat the published procedure as a model of the work, not proof of how every case unfolds. When access and authority allow, compare it with interviews, representative records, system events, observation, or a structured usability test.

When a worker adapts or bypasses a step, ask what conditions made that action reasonable at the time: unavailable tools, missing information, competing targets, unclear ownership, delays, or an unsafe or contradictory instruction. Separate:

- safe flexibility that should remain available;
- a risky workaround that needs a control or alternative path;
- a policy or authority question that only the owner can resolve;
- a one-off error whose cause is not yet known.

Do not silently turn a local workaround into an approved standard. Do not frame deviation as individual blame before examining conditions, controls, and resource constraints. If there is immediate danger, stop the test or operation and follow the approved safety route.

## Design controls around likely failure

Consider controls in this practical order, selecting what fits the risk and authority:

1. **Remove the unnecessary hazard or step.** Simplify the route while preserving required outcomes and controls.
2. **Prevent or constrain the error.** Use an approved validation, sequence rule, required field, permission boundary, interlock, or other control that blocks an unsafe transition.
3. **Detect the error in time to act.** Verify a critical value, source, identity, state, or handoff before the next consequential step.
4. **Warn and guide.** Put a specific warning beside the affected action and state what the user should do. A warning depends on attention and is weaker than a verified preventive control.
5. **Recover or mitigate.** Define how to stop, contain, reverse, compensate, escalate, or continue manually when prevention fails.

This is a design aid, not a formal safety hierarchy or a claim that a written control is implemented. Identify who owns each control and how it is verified in the actual process or runtime.

## Use checklists without replacing the procedure

A procedure explains the sequence, decisions, context, and exception paths. A checklist supports selected actions or confirmations at a pause point.

- Use **read-do** when the user should read each action and perform it in sequence.
- Use **do-confirm** when trained users perform a routine from memory and pause to confirm critical items before proceeding.
- Keep the checklist focused on error-prone, easily omitted, high-consequence, or coordination-critical items.
- Design it with the people who use it and place it near the work when practical.
- Avoid duplicating the full procedure in a checklist. There is no universal item count or pause duration.
- Keep judgment, exception handling, and authority visible; do not imply that checking a box makes a decision safe.

## Test usability with realistic work

Use `assets/sop-usability-test-plan.md` to prepare sessions. Test the document with people who represent the intended roles and conditions. Define success before testing, use objective scenarios, and observe where participants pause, misinterpret a condition, ask for help, take an unsafe path, or need information absent from the procedure.

Use simulation or a controlled environment when a live test could affect people, money, safety, access, service availability, or production data. Do not coach participants through the route unless safety requires intervention; record any intervention and its reason. Test a revised procedure again when the issue could affect outcome or safety. Report exactly which roles and cases were tested; do not generalize beyond them.

## Learn from incidents and near misses

Record a concise timeline, impact, operating conditions, signals available at the time, decisions and handoffs, controls that worked or failed, and contributing system factors. Identify corrective actions with an owner and verification method. Separate learning from disciplinary or legal processes, which follow their own authority and policies. Update the SOP only when a change to the procedure is a suitable preventive or recovery control.
