# Process discovery, analysis, and method selection

Use this reference to choose the right level of process detail and to prevent a diagram from standing in for understanding the work.

## 1. Set the boundary before mapping

Record:

- **Purpose:** the outcome the process exists to create and for whom.
- **Trigger:** what starts a case or execution.
- **Start and end:** observable boundary events, not vague department names.
- **Inputs and outputs:** information, materials, decisions, and services entering or leaving.
- **Actors:** roles that perform, decide, review, or receive the work.
- **Operating context:** systems, policies, jurisdictions, volumes, timing, and constraints that change the flow.
- **Evidence:** what comes from policy, a process owner, direct observation, sample records, system events, or inference.

If the boundary cannot be agreed, document competing boundaries and their consequences before drawing a detailed flow.

## 2. Select a method for the question

| Method | Use when | Avoid when |
| --- | --- | --- |
| SIPOC or equivalent scope table | Stakeholders need a shared high-level boundary, inputs, outputs, and customers | The question is about exact task order or detailed exception behavior |
| Value-stream map | End-to-end flow, wait time, queues, rework, and value delivery need comparison | A process is mainly a variable knowledge case with no useful common sequence |
| Simple flowchart or swimlane | A team needs a readable sequence, roles, decisions, and handoffs | A regulated or technically complex exchange requires a formal notation and validation |
| BPMN | A repeatable, structured workflow needs explicit events, roles, branches, and handoffs | The workflow is mostly discretionary or changes materially by case |
| DMN or decision table | A decision depends on multiple explicit conditions and outcomes | Decision rules are unknown, subjective, or not approved by their owner |
| Case-oriented model such as CMMN | Work is case-based, event-driven, and the next step varies with evidence and judgment | The flow is stable and a simpler sequence is clearer |

These are selection aids, not mandatory standards. Check the current specification and tooling when formal notation is required.

## Improvement approaches

Choose an improvement cycle that fits the evidence and decision:

| Approach | Useful when | Limit |
| --- | --- | --- |
| PDCA (plan, do, check, act) | A team can make a bounded change, observe the result, and adjust | A cycle label alone does not define a valid measure or prove causality |
| DMAIC (define, measure, analyze, improve, control) | The outcome can be operationally defined and measured, and variation or defects need analysis | Do not manufacture statistical certainty from weak, small, or biased data |
| Lean analysis | Waiting, handoffs, queues, duplicate work, or non-value-adding steps are plausible sources of friction | Define value with the recipient and preserve required controls; do not remove a step just because it looks indirect |
| Quality-at-source / continuous improvement | Multiple roles can prevent, detect, and learn from recurring errors | A slogan or workshop is not a substitute for control ownership and follow-through |

Use a method as a way to structure inquiry. State what data, decision owner, and follow-up would show whether a change helped.

## 3. Describe current state and proposed state separately

For current state, distinguish what people report from what a sample, observation, system record, or approved document confirms. Mark the sample and date; do not generalize from one case without saying so. Compare the prescribed process (work as imagined) with the process people actually perform (work as done). Ask what constraints, goals, handoffs, interruptions, and adaptations explain differences. A deviation is a signal to investigate, not automatic proof of negligence.

Analyze:

- queues, waits, duplicate entry, unnecessary movement, and rework;
- unclear ownership, handoffs, missing inputs, and decision delays;
- error opportunities, quality checks, security controls, and dependencies;
- variation between ordinary cases and exceptions;
- whether a control prevents an error, detects it, or helps recover after it.

Reliable event logs can help examine flow and timing, but show only activity captured by those systems. Combine them with interviews or observation where appropriate to identify manual work and workarounds. Use process-mining or task-activity data only when the organization has authority to use it, the data and sample are suitable, privacy and security controls are met, and the result is described within its coverage limits. Screen, audio, or video capture can expose sensitive information; do not treat it as a default discovery method.

For proposed state, describe each change, expected benefit, risk introduced, dependency, owner, and measure. Simplification ideas include removing an unnecessary step, combining compatible work, parallelizing independent work, routing by explicit criteria, and moving a decision to the role with sufficient context. Validate each idea with affected roles and control owners.

## 4. Pick the document unit

| Artifact | Main question it answers |
| --- | --- |
| Policy | What principles or boundaries govern decisions? |
| Process overview/map | What work crosses roles and how does it flow? |
| Procedure or SOP | Who performs a recurring process and in what sequence? |
| Work instruction | How does one role complete a specific task or tool operation? |
| Checklist | What critical items must be completed or confirmed? |
| Runbook | What concrete steps address a technical operation or known failure? |
| Playbook | What choices and actions fit a changing scenario? |

Link related artifacts when that reduces duplication. Do not force every process into a long SOP; use risk, frequency, variation, staff turnover, and user need as local decision factors, not universal thresholds.

## Clarify task ownership and decision rights

Name the role that performs each task and the role authorized to decide or approve it. A responsibility matrix can help when handoffs are unclear; choose a format the organization understands and define what its roles mean. If using RACI, assign a clear accountable role for each activity and confirm the responsible role has the access, capacity, and authority to perform it. For a contested or cross-functional decision, a decision-rights model may be clearer than extending a task matrix. Avoid large consulted/informed lists that add delay without changing the decision.

## 5. Define useful measures

Start with the intended outcome, then select a small set of indicators with an owner and a defined calculation. Depending on the process, measures may include completion quality, time to outcome, wait time, error or rework rate, safety events, customer outcome, adherence, or cost. Define the population, period, denominator, data source, and known limitations. Do not claim that access counts alone prove use or effectiveness.
