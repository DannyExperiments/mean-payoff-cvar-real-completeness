# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Simultaneous expectation and lower-tail CVaR is ∃ℝ-complete | [Theorem 1](paper/manuscript.pdf) |
| The flow and hinge formulation supplies membership | [Section 2 and source attribution](paper/manuscript.pdf) |
| Two opposite tail inequalities enforce xy = z | [Section 3.3](paper/manuscript.pdf) and [exact replay](verification/results/replay.txt) |
| Binary state rewards and a common rational interior level suffice for pure CVaR hardness | [Theorem 2 and Section 4](paper/manuscript.pdf) and [companion](proof/binary-reward-companion.md) |
| The source leaves the exact complexity gap | [Primary sources and comparison](audits/public_safe_reports/LITERATURE.md) |

## Lean verification

Lean checks the mass drawn from the pivot and proves that the two signed lower-tail integral bounds for the compressed branches are simultaneously met exactly when z equals x times y, at positive branch weight. The correspondence with stochastic strategies, membership and binary-reward reduction remain in the paper. [Source and replay](formalization/README.md)
