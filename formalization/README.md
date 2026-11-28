# Lean verification

Lean checks the mass drawn from the pivot and proves that the two signed lower-tail integral bounds for the compressed branches are simultaneously met exactly when z equals x times y, at positive branch weight. The correspondence with stochastic strategies, membership and binary-reward reduction remain in the paper.

The checked declaration is `TailGadget.multiplication`. [Source](TailGadget.lean) · [Pinned CI](../.github/workflows/lean.yml)

```sh
lean -DwarningAsError=true formalization/TailGadget.lean
```

CI compares the compiler output with the committed axiom report.
