# ADR-002: Prepare Tester acceptance-criteria verification for deterministic conversion



## Status



Proposed



## Context



The Tester runs after the Reviewer passes an implementation and before the workflow can continue to the Project Manager. It receives the acceptance criteria, modified-file list, and implementation summary, runs the available test suite, and determines whether the results adequately satisfy each acceptance criterion.



Iteration Log Run 2 (2026-08-10) shows that this step provides more than mechanical test execution. The Tester identified that several acceptance criteria lacked automated coverage, including localStorage persistence, product-specific review rendering, and cascade deletion of reviews when a product is removed. It blocked completion until the Implementer added the missing tests.



The mechanical portions of this step, such as running tests and reporting passed, failed, and skipped counts, appear specifiable. However, the evidence does not yet demonstrate stability across at least two full calibration cycles or repeatability across repeated identical inputs, and interpreting whether tests adequately cover natural-language acceptance criteria still requires judgment.



## Decision



Keep the complete Tester acceptance-criteria verification step agentic for now while treating its mechanical test-running and result-counting portions as potential deterministic conversion candidates after additional calibration and repeatability evidence is collected.



## Alternatives Considered



### Alternative 1: Convert the complete Tester step to deterministic code now



Rejected for now. The available evidence does not demonstrate stability across at least two full calibration cycles or identical decisions across repeated runs on unchanged input. In addition, Iteration Log Run 2 shows that the Tester had to recognize missing acceptance-criteria coverage even though the issue was not simply a failing test.



### Alternative 2: Keep the entire Tester step agentic



Viable for now, because interpretation of natural-language acceptance criteria still requires judgment. However, keeping purely mechanical operations such as test execution and result counting inside the agent may retain unnecessary inference and governance overhead if those portions prove fully specifiable.



### Alternative 3: Convert only the mechanical portions and retain agent judgment for coverage verification



Preferred future direction, pending evidence. Test execution and passed/failed/skipped result collection could potentially become deterministic while the agent continues to determine whether the available tests adequately cover each acceptance criterion. This preserves the judgment demonstrated in Iteration Log Run 2 without requiring an agent for operations that may have one predictable result.



## Consequences



The immediate consequence is that no implementation changes will be made as part of this exercise. The Tester remains responsible for acceptance-criteria verification.



A future partial conversion could reduce inference work and make test execution and result counting more predictable and easier to audit. The trade-off is that splitting deterministic execution from agentic interpretation creates a new interface whose output shape would need to remain compatible with the Tester and Orchestrator.



The known behavior that must be preserved is the ability to detect when a test suite has no failing tests but still leaves an acceptance criterion uncovered. A deterministic replacement must not silently convert that situation into PASS.



## Evidence



- `docs/iteration-log.md`, Run 2 - Full Product Review workflow, dated 2026-08-10: the Tester identified missing automated coverage for localStorage persistence, product-specific review rendering, and cascade deletion, blocked completion, and returned PASS only after the missing tests were added.

- `agents/tester.md`: defines the Tester's inputs, read-only tool boundary, responsibility to compare test results against each acceptance criterion, and PASS/FAIL output contract.

- `docs/step-classification.md`, Tester acceptance-criteria verification entry, committed in `59914f9`.

- Before-and-after conversion measurements do not exist yet because this ADR is Proposed and this exercise stops before implementation.


