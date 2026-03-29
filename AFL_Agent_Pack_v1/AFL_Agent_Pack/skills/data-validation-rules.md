# Data Validation Rules

## Purpose
Fail bad content before it becomes production debt.

## Required AFL checks
- bad naming
- wrong folder placement
- missing collision on arena blockers
- missing gameplay tags
- missing objective anchors
- missing broadcast anchors
- invalid reward table fields
- invalid audio metadata
- invalid Data Layer usage

## Procedure
1. Define the rule in prose.
2. Decide whether it can be checked in Python, Unreal Data Validation, or both.
3. Add a repo-side validator when the rule does not require editor state.
4. Make the failure message actionable.

## Deliverables
- rule definition
- checker implementation
- fix guidance

## Validation
- checker returns non-zero on real failures
- false positives are documented and minimized
