---
title: "[Agent procedure title]"
version: "0.1"
status: "draft"
owner_role: "[Process/system owner role]"
approver_role: "[Approving role or TBD]"
effective_date: "[YYYY-MM-DD or TBD]"
review_by: "[YYYY-MM-DD or event trigger]"
scope: "[Short boundary]"
execution_mode: "[assisted / bounded execution / hybrid]"
---

# [Agent procedure title]

## Objective and outcome

[Task, intended outcome, and verifiable completion condition.]

## Scope

- **Trigger:** [What starts a run or case.]
- **Eligible cases:** [In-scope conditions.]
- **Excluded cases:** [Out-of-scope conditions and destination.]
- **Start and end:** [Observable boundaries.]

## Inputs and preconditions

| Input | Authoritative source | Validation and freshness | Missing/conflicting value |
| --- | --- | --- | --- |
| [Input] | [Source] | [Check] | [Stop/escalate] |

## Roles and responsibilities

| Role or runtime identity | Responsibility | Authority boundary |
| --- | --- | --- |
| [Role/runtime] | [Action] | [Allowed authority] |

## Tools, data, and permissions

- **Available tools:** [Verified capabilities only.]
- **Allowed data:** [Minimum necessary data and access basis.]
- **Allowed actions:** [Explicit action and scope.]
- **Prohibited actions:** [Explicit list.]
- **Dependencies:** [System, policy, human coverage, or approval.]
- **Runtime enforcement:** [Verified permission boundary, allowlist, time/iteration/cost limits, timeout, and stop control where available; mark unsupported controls as pending.]
- **Versioned components:** [Agent/model, prompt, tool, policy, or workflow version identifiers when available.]

## Procedure

1. Validate the trigger, case scope, identity, and required inputs. Stop if a required check fails.
2. Retrieve only the permitted information from the approved source. Record source references, not unnecessary sensitive content.
3. Apply the approved decision rule: [rule and owner]. If the rule is missing, conflicting, or does not cover the case, stop and escalate to [role].
4. Prepare the proposed action and show the human reviewer [evidence, decision, impact, and uncertainty]. Wait for required approval before any consequential side effect.
5. Perform only the approved action within the verified permission boundary. Confirm the result and prevent unintended duplicate action where applicable.
6. Record the outcome and close the case only when [completion condition] is confirmed.

## Success criteria and controls

- **Completion condition:** [Observable result.]
- **Pre-action check:** [Identity, policy, data, permission, and approval checks.]
- **Post-action check:** [Result confirmation and duplicate/error check.]
- **Audit evidence:** [Minimum necessary record and access policy.]

## Autonomy and prohibited actions

- **Autonomous actions allowed:** [Exact actions and conditions, or “none.”]
- **Actions requiring approval:** [Exact action and approver role.]
- **Prohibited actions:** [Actions the system must not take.]
- **Hard limits:** [Approved policy values; use TBD until confirmed.]

## Human oversight

Reviewer role must have enough context, time, competence, and authority to correct, reject, or stop the proposed action. Do not count a confirmation click alone as effective review.

| Escalation trigger | Human role | Information presented | Decision required |
| --- | --- | --- | --- |
| [Trigger] | [Role] | [Evidence and uncertainty] | [Approve/reject/correct/route] |

## Failures, fallback, and recovery

| Failure or unsafe condition | Stop/retry rule | Recovery or fallback | Owner |
| --- | --- | --- | --- |
| [Condition] | [Safe condition for retry or stop] | [Rollback, manual route, or no action] | [Role] |

## Records, audit, and monitoring

[Define minimum event fields, access, retention authority, alert owner, review cadence/trigger, and handling of sensitive content.]

## Evaluation and release criteria

- [ ] Normal, variation, boundary, failure, and adversarial cases have expected results.
- [ ] Untrusted content cannot expand instructions or permissions; prompt or goal hijacking cases are tested where relevant.
- [ ] Permissions and denied actions were checked in the target runtime.
- [ ] Human approval and escalation routes have accountable coverage and reviewer capacity.
- [ ] Monitoring, error handling, duplicate protection, and recovery were tested where applicable.
- [ ] Process owner and system/control owners reviewed the release evidence.
- [ ] Disable or rollback procedure is available.

## Governance and references

- **Process owner:** [Role]
- **System owner:** [Role]
- **Approver and status:** [Role/status]
- **Version, effective date, review trigger:** [Values]
- **Change history:** [Date, change, reason, approver]
- **References:** [Current approved policy/specification and relevant section]
