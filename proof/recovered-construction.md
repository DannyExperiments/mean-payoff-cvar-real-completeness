# Q668: Multi-dimensional expected mean-payoff and lower-tail CVaR is existential-real complete

For the exact decision problem in the catalog, with rational finite MDPs, state rewards and liminf mean payoff, the complexity is ∃ℝ-complete under polynomial-time many-one reductions. Thus NP suffices if and only if NP=∃ℝ. Hardness persists with bounded nonnegative integer state rewards, all tail levels 1/2, and one initial stochastic choice leading to either a simple randomized choice or a closed two-state component.

## Lower-tail convention

For bounded X, the average of its lowest p probability mass, splitting atoms fractionally, is
  CVaR_p(X) = max_t [t − E[(t−X)_+]/p].
The expression is maximized at any p-quantile: the left and right slopes are 1−P(X<t)/p and 1−P(X≤t)/p, and evaluation there gives the fractional tail integral. In particular replacing X by its conditional mean given any finite label can only increase lower-tail CVaR, by Jensen applied to the hinge for each t. The unconditional expectation is unchanged.

## Membership in ∃ℝ

Use [Křetínský and Meggendorfer, Lemma 6.7 and Theorem 6.8](https://arxiv.org/pdf/1805.02946#page=9): one may take a policy with deterministic payoff conditional on the eventual maximal end component (MEC), and the feasible probability masses and recurrent frequencies for such a strategy are given by the transient and recurrent linear flows (1)–(4) in their Fig. 9. In these flows the stopping/commit mass variables y_s are zero outside MECs, and recurrent frequency variables concern only actions staying inside a MEC. For each MEC i, let w_i be its total commit mass, equivalently the sum of its unnormalized recurrent state frequencies x_s. Their argument realizes the frequencies with a policy that yields the corresponding mean vector almost surely conditional on that component. Thus for w_i>0 the payoff value for dimension j is v_ij=(Σ_{s in i} x_s r_j(s))/w_i. Impose the usual expected-payoff bound Σ_s x_s r_j(s)≥e_j.

Add an existential cutoff t_j and nonnegative hinge variables H_ij with
  H_ij ≥ w_i t_j − Σ_{s in i} x_s r_j(s),
  p_j t_j − Σ_i H_ij ≥ p_j c_j .
The first right-hand side is w_i(t_j−v_ij) for positive component mass, and zero if w_i=0. The smallest H_ij is exactly the weighted hinge from the displayed CVaR identity, so this is equivalent to each CVaR bound. The flows plus these inequalities form a polynomial-size existential real formula of degree at most two. This makes explicit the paper's existing real-algebraic method (it states the PSPACE consequence); the new part is the matching hardness.

## Hardness source

Start with [Abrahamsen, Adamaszek and Miltzow's ETR-INV](https://arxiv.org/abs/1704.06969), an ∃ℝ-complete system on variables v_i∈[1/2,2] with constant-one, addition and reciprocal equations. Substitute v_i=(1+3x_i)/2 with x_i∈[0,1]. Constant and addition equations become rational linear equalities. For a reciprocal equation v_i v_j=1 introduce w∈[0,1] and encode x_i x_j=w and 3w+x_i+x_j=1. Thus it suffices to implement simultaneous linear equalities and equations of the form xy=z for bounded variables. Coefficients of the converted linear equalities are bounded integers after clearing denominators.

## MDP and expectation coordinates

There are N variables. Let h=1/(16N), and put mass h on each of five initial branches for each variable i. The first branch of i leads to a choice with two actions: go to absorbing L_i or H_i. A policy induces conditional probability x_i∈[0,1] of L_i, so its unconditional mass is hx_i. The other four branches go to four disjoint closed two-state components for i, labelled pivot, comp-x, comp-y and comp-z. Both states have two actions, allowing the next state to be deterministically 0 or 1. Add two absorbing padding branches to the initial stochastic choice: low padding of mass b=1/2−4h≥0 and high padding of mass 1−5Nh−b>0. The branch laws are rational and independent of policy decisions. All initial or transient rewards can be set zero before final uniform shifts; prefixes vanish in long-run means.

For each component copy of i, let F_n be the fraction of state 1. To force frequency agreement with x_i, use an expectation constraint E[X]≥0 with reward +1 at state 1 of that copy and −1 at L_i, zero elsewhere, and a second expectation constraint with opposite rewards. Their two expectations are h(E[liminf F_n | copy]−x_i) and h(x_i−E[limsup F_n | copy]). These being nonnegative force conditional expectation equality and a.s. convergence of F_n, with conditional mean x_i, since limsup≥liminf. This applies independently to all four copies and works for arbitrary history-dependent policies. Enforce a linear equation in x_i by two opposite expectation bounds on weighted indicators of L_i, using the known h. The trivial CVaR constraint for each expectation dimension can be set at or below its minimum possible state reward.

Conversely, any variable assignment x∈[0,1]^N can be realized: choose L_i with probability x_i and, in each copy of i, use stationary randomized actions making the next state i.i.d. Bernoulli(x_i). The frequency then equals x_i almost surely in the limit, including endpoints.

## Multiplication coordinates

Take an equation xy=z, with variable indices not necessarily distinct. Use two risk coordinates, one for each sign σ=+1,−1, with all expectations trivial. Analyze constant branch means first. In the chosen coordinate set the payoffs by branch as follows:
- low padding: −2;
- L_x: 3;
- comp-x copy of x: 2x;
- comp-y copy of y: −σ y;
- comp-z copy of z: σ z;
- pivot copy of y: 5+σ y;
- every other branch: 9.

An affine branch reward u+v x_i is represented by state rewards u and u+v in the selected two-state copy. Distinct role copies remain different even for repeated variables. The ordering is fixed across all assignments: each comparison copy lies in [−1,2], then L_x pays 3, the pivot pays in [4,6], and the high outcomes pay 9. The lowest half has the padding b, then the three compensation masses h each and the low mass hx, then h(1−x) from the pivot. At endpoints the fraction can be zero or all of the pivot. Thus its total payoff integral is
  −2b + h[3x+2x−σ y+σ z+(1−x)(5+σ y)]
  = −2b + h[5+σ(z−xy)].
Set the lower-tail CVaR threshold to 2(−2b+5h) in both coordinates, since the tail mass is 1/2. This forces z−xy to have both signs nonnegative, hence z=xy.

For arbitrary satisfying strategies the expectation coordinates imply a.s. frequency convergence in the copies and the stated conditional means. Their branch payoffs within a copy need not be deterministic. Compress the payoff law conditional on the terminal branch (distinguishing L_i and H_i separately) to its conditional means. The Jensen argument at the start improves every lower-tail criterion simultaneously; for these means the equation calculation above applies and forces the original algebraic system. This proves soundness without assuming finite-memory sufficiency for the lower bound. For completeness the stationary strategies described earlier make each conditional copy payoff constant and exactly meet the thresholds. The two implications establish feasibility equality.

Rewards can all be made nonnegative by adding the same constant to every state reward within a coordinate and shifting both thresholds. The reduction uses bounded coefficients and rewards, polynomially many states and payoff dimensions, and rational thresholds described with polynomially many bits. Real randomized policies are allowed under the catalog semantics. In fact the same gadget for x²=1/2 gives rational input with a forced irrational conditional action probability x=1/√2 at a unique start history; this is not by itself a complexity lower bound.

## Source scope

[Original LICS paper](https://doi.org/10.1145/3209108.3209176) gives the previous NP-hardness/PSPACE gap for multiple expectation/CVaR constraints; [Meggendorfer's thesis](https://mediatum.ub.tum.de/doc/1550256/lkmnxpqo0rgh35wrrilavbv8a.Tobias_Meggendorfer_PhD_Thesis.pdf) discusses this and the NP question. The classification above is for lower-tail CVaR of the long-run liminf payoff with fractional atoms, not VaR, discounted cumulative rewards or finite-horizon terminal rewards. The result is not an unconditional separation from NP or a priority claim.
