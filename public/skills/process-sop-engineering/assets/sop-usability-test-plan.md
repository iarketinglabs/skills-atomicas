# SOP usability test plan

Use this plan to check whether intended users can apply a procedure in representative conditions. It does not establish formal approval or compliance by itself.

## Test setup

- **Procedure and version:**
- **Process owner and test lead roles:**
- **Question the test should answer:**
- **Intended user roles and relevant experience:**
- **Environment:** live / simulated / sandbox
- **Risk controls and stop rule:** [How the test will avoid real-world harm]
- **Known limitations:** [Roles, cases, or conditions not represented]

## Success criteria

Choose criteria before the session. Use only measures that help decide whether to revise, pilot, or approve the procedure.

- **Expected outcome:**
- **Critical errors that must not occur:**
- **Required checks, decisions, or escalations:**
- **Help or clarification allowed:**
- **Time measure, if time affects the outcome:**
- **Release decision owner:**

## Scenarios

| Scenario | Starting information | Expected outcome or safe stop | Variation/failure tested | Evidence source |
| --- | --- | --- | --- | --- |
| Normal case | [Representative inputs] | [Observable result] | [Optional] | [Policy, sample, or owner decision] |
| Exception | [Missing, conflicting, or unusual input] | [Safe route or escalation] | [Condition] | [Source] |
| Dependency/control failure | [Unavailable tool or failed check] | [Stop, recovery, or manual route] | [Condition] | [Source] |

Do not include live personal, financial, confidential, or production data unless authorized and necessary. Use approved synthetic or redacted examples when possible.

## Session protocol

1. Tell the participant the test evaluates the procedure, not their competence. Explain the scenario, environment, and safety stop rule.
2. Give a neutral task statement. Do not name the exact step or point to the answer.
3. Observe the participant using the procedure. Record pauses, interpretation questions, rework, missed checks, escalation choices, and unsafe or unexpected paths.
4. Do not coach. If a real safety or service risk appears, intervene, stop the session, and record why.
5. Ask what information was missing, unclear, hard to find, or inconsistent with the actual work.
6. Compare observations with the predeclared success criteria. Record findings, severity, evidence, owner, and disposition.

## Results and decision

| Finding | Scenario and evidence | Impact | Owner | Action | Retest needed? |
| --- | --- | --- | --- | --- | --- |
| [Issue or successful result] | [Observation] | [Outcome/risk] | [Role] | [Change or rationale] | Yes / No |

- **Decision:** revise / retest / pilot / submit for approval / no change, with rationale
- **Unresolved risks or assumptions:**
- **Roles and scenarios not tested:**
- **Approval status:** [Use locally defined status; testing is not approval]
