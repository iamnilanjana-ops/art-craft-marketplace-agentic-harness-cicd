\# ADR-003: Rubric Design for Agentic Evaluation



\## Status



Accepted



\## Context



The agentic engineering pipeline needs an evaluation method that can judge output quality consistently across different workflow runs.



Deterministic checks are useful for structural requirements such as schema validity, routing, policy enforcement, and required files, but they cannot fully evaluate qualitative properties such as whether an answer is correct, sufficiently grounded in retrieved evidence, focused on the requested task, or clear enough for a human reviewer to act on.



The capstone therefore requires a rubric-based evaluation layer that complements deterministic checks rather than replacing them.



The evaluation design also needs to be simple enough to apply repeatedly during calibration and regression testing.



\## Decision



Use a four-dimension rubric with a 1–4 scoring scale.



The rubric dimensions are:



1\. \*\*Correctness\*\* — whether the final output performs the requested task without significant errors or omissions.

2\. \*\*Task Adherence\*\* — whether the workflow stays within the requested scope instead of performing unrelated work.

3\. \*\*Groundedness\*\* — whether claims based on retrieved information accurately reflect the supporting sources.

4\. \*\*Clarity\*\* — whether the output is organized and actionable without unnecessary rework.



Each dimension has a minimum passing score of:



```text

3

```



The overall passing threshold is:



```text

12

```



This means a run must meet the acceptable threshold across all four dimensions rather than compensating for a weak dimension with a high score elsewhere.



The rubric is stored in:



```text

eval/rubric.json

```



Each dimension contains:



\* a description;

\* a pass threshold;

\* scoring definitions for levels 1–4;

\* examples illustrating weak and strong outcomes.



\## Rejected Alternatives



\### Alternative 1: Use only deterministic pass/fail tests



Rejected because deterministic checks can verify structure and policy rules but cannot reliably judge qualitative output such as reasoning quality, clarity, relevance, or grounded use of retrieved evidence.



A workflow could pass every structural test while still producing an unclear or poorly grounded result.



\### Alternative 2: Use one overall quality score



Rejected because a single score would hide the reason a run failed.



For example, a response could be technically correct but drift outside the task, or it could be clear but poorly grounded.



Separating the rubric into dimensions makes failures easier to diagnose and gives calibration work a specific target.



\### Alternative 3: Use a larger or more complex rubric



Rejected because additional dimensions would increase scoring overhead without clear evidence that more categories were necessary for this workflow.



The current four dimensions cover the major qualitative risks while remaining practical for repeated evaluation.



\## Evidence



The rubric is implemented in `eval/rubric.json` with four dimensions:



\* correctness;

\* task adherence;

\* groundedness;

\* clarity.



Each dimension requires a score of at least 3, and the overall passing threshold is 12.

The threshold of 12 is intentional because there are four quality dimensions and each dimension must score at least 3. A total of 12 therefore represents the minimum acceptable result of 3 + 3 + 3 + 3.

This prevents a high score in one area from hiding a serious weakness in another. For example, a run should not pass merely because it is very clear if it is incorrect or poorly grounded.

From a business perspective, this threshold reduces reviewer rework by requiring every passing result to be independently acceptable for correctness, task adherence, groundedness, and clarity before it moves forward. Scores below 3 in any dimension indicate that additional review or correction is still needed.


Calibration evidence also shows that the wider evaluation system is used alongside deterministic and policy checks rather than in isolation.



The calibration log records a successful integrated regression check with:



```text

24/24 harness checks passing

```



and the policy suite passing.



The same calibration evidence records real workflow near-misses involving:



\* excessive implementer permissions;

\* reviewer skill overreach;

\* retrieval beyond a role's classification ceiling.



These failures demonstrate why evaluation must measure more than whether a task merely produced output.



\## Consequences



\### Positive consequences



\* Evaluation failures can be traced to a specific quality dimension.

\* Calibration changes can target the relevant weakness instead of changing the entire workflow.

\* The rubric complements deterministic validation and policy tests.

\* A score of 3 provides a clear minimum acceptable quality level.

\* Explicit examples make scoring more repeatable.

\* Groundedness ensures retrieval quality is reflected in final outputs rather than measured only at the retrieval layer.



\### Negative consequences



\* Rubric scoring may require an agent or human evaluator.

\* Qualitative scoring can still contain some judgment variability.

\* The rubric increases evaluation cost compared with deterministic checks alone.

\* Examples may need to evolve if the workflow changes significantly.



\## Open Risks



1\. Rubric-based scoring may vary slightly across evaluator models or repeated scoring runs.

2\. The current rubric may not capture specialized reviewer or tester concerns if those roles require more detailed future evaluation.

3\. A model-based judge could incorrectly score an output even when deterministic evidence suggests a different conclusion.

4\. Changes to the workflow may require new examples or additional dimensions.



These risks are mitigated by keeping deterministic checks as the first evaluation layer and treating rubric scoring as a complementary qualitative layer rather than the sole source of truth.



\## Decision Summary



The pipeline will use a four-dimension, 1–4 rubric with a minimum score of 3 per dimension and an overall passing threshold of 12.



This design was selected because it provides enough qualitative detail to diagnose failures while remaining simple enough to use repeatedly during calibration and regression testing.



