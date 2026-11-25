# Procedure review checklist

Mark each item **Pass**, **Needs work**, **Not applicable**, or **Not verified**. Record evidence or an owner for every item that needs work. A checklist result does not equal approval.

## Purpose and boundary

- [ ] Intended outcome and completion condition are observable.
- [ ] Trigger, start, end, in-scope cases, and out-of-scope routing are explicit.
- [ ] Audience and required knowledge are clear.
- [ ] Current-state facts are distinguished from proposals and assumptions.
- [ ] Differences between written and actual work were investigated where evidence was available; deviations were not treated as individual blame by default.
- [ ] Workarounds have an owner and disposition; unsafe or unauthorized workarounds are not silently adopted as the new standard.

## Roles and execution

- [ ] Each action and decision has a role owner.
- [ ] Inputs, prerequisites, tools, outputs, and handoffs are named.
- [ ] Steps begin with precise actions and can be followed in order.
- [ ] Conditions, branches, decision criteria, and success checks are explicit.
- [ ] Missing input, tool failure, exceptions, stop points, and escalations are covered.
- [ ] Controls are placed at the relevant step and have an owner.
- [ ] Critical controls prevent or detect errors where feasible; warnings are not the only safeguard when the risk needs a stronger control.
- [ ] Stop, recovery, and manual fallback actions are usable and authorized.

## Safety, data, and governance

- [ ] Permissions and approval boundaries are explicit.
- [ ] Sensitive information is limited to what is necessary and handled by approved rules.
- [ ] Legal, safety, regulatory, quality, and security claims have current applicable sources or are marked pending.
- [ ] Owner, approver, version, status, effective date, review trigger, and change history are present or marked TBD.
- [ ] Adoption, training, record location, and retirement/supersession are addressed.

## Agent or automation additions

- [ ] Only verified tool capabilities are described.
- [ ] Allowed, prohibited, and approval-required actions are separate.
- [ ] Identity, inputs, validation, failure handling, and duplicate-action behavior are defined.
- [ ] Human oversight, uncertainty handling, escalation, and manual fallback are defined.
- [ ] Logs, monitoring, retention, evaluation cases, release checks, and rollback are defined.
- [ ] Instructions do not claim runtime enforcement that has not been tested.
- [ ] Reviewers have relevant evidence, time/capacity, competence, and authority to reject, correct, or stop an agent action.
- [ ] Evaluation includes out-of-scope input, tool/permission failure, and an unsafe or adversarial input where relevant.

## Walk-through and status

- [ ] A normal case was walked through or the absence of a walk-through is stated.
- [ ] At least one exception, boundary, or failure case was considered.
- [ ] Usability testing used representative roles and neutral scenarios, or its absence and limits are stated.
- [ ] Findings have owners and disposition.
- [ ] Status accurately says draft, reviewed, piloted, approved, or another locally defined state.
