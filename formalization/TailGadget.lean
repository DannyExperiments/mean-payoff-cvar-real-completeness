import Std
namespace TailGadget
open Lean.Grind Std
variable {R : Type} [CommRing R] [LE R] [LT R] [IsLinearOrder R] [LawfulOrderLT R] [OrderedRing R]

/-- Lowest-half payoff integral once the L and pivot branches have been ordered. -/
def integral (s x y z h b : R) :=
  -2*b + h*(2*x - s*y + s*z + 3*x) + h*(1-x)*(5+s*y)

omit [LE R] [LT R] [IsLinearOrder R] [LawfulOrderLT R] [OrderedRing R] in
theorem pivot_mass (x h b : R) (half : R) (mass : b+4*h=half) :
    half - (b+3*h+h*x) = h*(1-x) := by grind

theorem multiplication (x y z h b : R) (pos : 0 < h) :
    (-2*b+5*h ≤ integral 1 x y z h b ∧ -2*b+5*h ≤ integral (-1) x y z h b) ↔
    x*y=z := by
  have q (s : R) : integral s x y z h b = -2*b+5*h+s*(h*(z-x*y)) := by
    unfold integral; grind
  rw [q,q]
  constructor
  · rintro ⟨hp,hm⟩
    apply Classical.byContradiction
    intro hx
    by_cases hlo : x*y < z
    · have H := OrderedRing.mul_pos pos (show 0 < z-x*y by grind)
      grind
    · have H := OrderedRing.mul_pos pos (show 0 < x*y-z by grind)
      grind
  · intro hz; rw [hz]; grind
end TailGadget
#print axioms TailGadget.pivot_mass
#print axioms TailGadget.multiplication
