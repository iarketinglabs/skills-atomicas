---
name: process-sop-engineering
description: Use this skill whenever someone asks to map, analyze, standardize, document, improve, validate, govern, or retire a business or operational process, SOP, procedure, work instruction, checklist, runbook, playbook, or workflow involving people, scripts, automation, or AI agents. Select a fit-for-purpose method, produce usable operating documentation, and make evidence, risks, ownership, exceptions, and human oversight explicit.
---

# Process and SOP engineering

Design and improve processes and operating documents for any organization, sector, or team. Keep the work outcome-focused: a document is useful only when the people or systems responsible can use it safely and consistently.

## Workflow

1. **Define the deliverable and boundary.** Identify the requested output, audience, execution mode, trigger, start and end points, intended outcome, constraints, and available evidence. Choose the smallest useful artifact: process overview/map, procedure, task instruction, checklist, runbook, playbook, or a combination. See `references/process-analysis-and-method-selection.md`.
2. **Inspect the evidence.** Read supplied policies, existing procedures, examples, logs, and user decisions that are accessible in the current runtime. Separate confirmed facts, observed evidence, inferences, proposals, and unknowns. Preserve conflicts and provenance; do not silently resolve them. See `references/evidence-and-governance.md`.
3. **Discover the current work.** Capture actors by role, inputs, outputs, handoffs, systems, decision points, normal path, exceptions, controls, failure modes, and measures. Compare prescribed work with work as actually performed when evidence is available. Investigate why workarounds or deviations exist before classifying them as individual error; they may reveal missing tools, conflicting goals, unsafe controls, or undocumented risk. Do not claim to have observed a process when you only have a description. Read `references/human-factors-and-usability.md` for this analysis.
4. **Choose a design method.** Select mapping and analysis methods that fit process stability, complexity, and the decision being made. Avoid using every framework by default. Distinguish current state from proposed state and identify why each proposed change improves the outcome.
5. **Set the execution and risk boundary.** Decide whether the procedure is for people, deterministic automation, an AI agent, or a hybrid. Evaluate variability, consequence of error, reversibility, data sensitivity, exception handling, permissions, and monitoring. For agent or automation work, read `references/human-agent-and-automation.md` and use `assets/agent-procedure-template.md` when applicable.
6. **Draft the operating document.** Use active voice, one action per step, defined terms, role-based owners, explicit decision criteria, expected outputs, and safe stop or recovery instructions. Prefer a control built into the process over a warning that depends on memory alone. Start from `assets/sop-template.md`; adapt its structure to the audience and risk. Use `assets/sop-review-checklist.md`.
7. **Validate the procedure.** Walk through representative normal, alternate, failure, and exception cases with people who perform or own the work. For a usability test, set success criteria first, use realistic non-leading scenarios, observe without coaching, and use a simulation when live testing could cause harm. Read `assets/sop-usability-test-plan.md` and `references/human-factors-and-usability.md`. Check whether inputs, decisions, outputs, controls, permissions, escalation, and recovery are actionable. Label the result as drafted, reviewed, piloted, or approved according to evidence; never imply approval that did not occur.
8. **Plan adoption and maintenance.** Assign a process owner and approver role, version, effective date, review date or review trigger, change history, access location, training needs, and outcome measures. Define how a changed or retired procedure is identified and archived. See `references/sop-lifecycle-and-quality.md`.
9. **Deliver the result with its limits.** State what was produced, assumptions and unresolved decisions, source status, validation performed, and next owner action. Create or edit local artifacts only when the runtime provides file access and the user requested the work. Do not publish, send, modify live systems, or execute an automation unless explicitly authorized and supported.

## Operating rules

- Ask a concise question only when a missing decision changes process scope, safety, ownership, or the artifact. Otherwise draft with visible assumptions and mark placeholders for confirmation.
- Keep names, examples, data, paths, and policy choices organization-neutral unless the user supplies organization-specific information for the current task. Never carry private details from one organization into another.
- Write in the user's requested language and explain specialist terms for the intended audience.
- Do not treat a template, notation, checklist size, step count, or time threshold as a universal standard. The source synthesis behind this skill flags several commonly repeated heuristics as unverified; use them only as local choices with an identified owner. See `references/evidence-and-governance.md`.
- Do not invent current law, standard clauses, certifications, tool capabilities, or compliance status. When current requirements matter, check primary or official sources if browsing is available; otherwise label the gap and request qualified review. Keep jurisdiction and edition visible.
- Preserve necessary controls while removing avoidable waiting, duplicate entry, rework, unclear handoffs, and unnecessary approval layers. Do not automate a broken or poorly understood process as a substitute for redesign.
- Treat deviations and near misses as evidence about the process and operating conditions. Preserve safe adaptations when appropriate; resolve unsafe or unauthorized workarounds with the process owner before documenting a new standard.
- Prefer the least complex execution design that meets the outcome. Use a deterministic workflow for stable, explicit rules; add an agent only when contextual variation justifies it and safeguards can be verified. Do not present autonomy-level labels as a universal scale.
- Use role names rather than personal names for durable responsibility assignments. Include a named contact only when requested and supported by supplied evidence.
- For high-impact, irreversible, regulated, safety-critical, financial, or sensitive-data actions, make the authorization boundary, human decision point, stop condition, escalation route, and recovery path explicit. Do not infer approval thresholds.
- Make human oversight operational: identify a reviewer with the information, time, competence, authority, and practical ability to correct, reject, or stop the action. An approval button alone is not evidence of effective review.
- Treat agent instructions as operational constraints, not proof of runtime enforcement. State which checks depend on tools, policies, logs, or human review that are not available in the current environment.
- Do not assign blame in incident analysis. Describe system conditions, contributing factors, impact, and corrective actions.

## Default deliverable

Unless the user requests another format, return:

1. A short process boundary and intended outcome.
2. The process map or operating procedure, with roles, steps, decisions, outputs, controls, exceptions, and stop/escalation conditions.
3. Assumptions, evidence gaps, and decisions that need an owner.
4. Validation status and a practical maintenance/adoption plan.

For a review-only request, prioritize findings by operational impact and point to the relevant step or section. For a process map, use a simple readable format supported by the runtime; a text table is acceptable when diagrams are unavailable.

## Bundled resources

- Read `references/process-analysis-and-method-selection.md` when selecting a mapping or redesign method.
- Read `references/sop-lifecycle-and-quality.md` when writing, testing, publishing, adopting, measuring, or retiring a procedure.
- Read `references/human-agent-and-automation.md` when the workflow includes scripts, RPA, AI agents, or mixed human-machine execution.
- Read `references/human-factors-and-usability.md` when work varies in practice, error prevention matters, or the procedure needs human testing.
- Read `references/evidence-and-governance.md` when claims, standards, regulation, approvals, or source quality matter.
- Use `assets/process-discovery-brief.md` to structure discovery; `assets/automation-decision-matrix.md` to compare execution modes; `assets/sop-usability-test-plan.md` to prepare validation; and the SOP templates and checklist for deliverables.
- Run `python scripts/validate_sop.py <file>` for a structural check of a generated Markdown procedure. Add `--profile agent-ready` for an agent procedure. This checks document structure only; it does not verify correctness, compliance, safety, or runtime behavior.
- Use `evals/evals.json` and `evals/scoring-rubric.md` to assess representative outputs. Evals are prompts and review criteria, not proof of performance until run in the target runtime.

## Runtime compatibility

Use only file, browser, database, code, or integration capabilities that the active runtime actually exposes. If a capability is absent, provide a reviewable document or instructions for the responsible person instead of implying an external action occurred. Adapt output format to the user; the bundled Markdown files are portable starting points, not platform requirements.
