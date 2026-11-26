"""Exact finite checks of the CVaR reduction and its binary-reward companion."""

from fractions import Fraction as F
from itertools import combinations_with_replacement, product


def tail_integral(atoms, level):
    """Lowest level mass, allowing a fraction of an atom at the cutoff."""
    assert sum(mass for _, mass in atoms) == 1
    assert all(mass >= 0 for _, mass in atoms)
    remaining, total = level, F(0)
    for value, mass in sorted(atoms):
        used = min(mass, remaining)
        total += used * value
        remaining -= used
        if remaining == 0:
            break
    assert remaining == 0
    return total


def check_multiplication():
    h = F(1, 80)
    padding = F(1, 2) - 4*h
    values = [F(i, 16) for i in range(17)]
    checked = 0
    for x, y, z in product(values, repeat=3):
        for sign in (-1, 1):
            atoms = [(-2, padding), (3, h*x), (2*x, h), (-sign*y, h),
                     (sign*z, h), (5+sign*y, h)]
            atoms.append((9, 1-sum(mass for _, mass in atoms)))
            assert tail_integral(atoms, F(1, 2)) == -2*padding+h*(5+sign*(z-x*y))
            checked += 1
    print(f"{checked} exact multiplication-tail identities including endpoint atoms")


def check_common_tail_levels():
    levels = sorted({F(i, denominator) for denominator in range(2, 13)
                     for i in range(1, denominator)})
    checked = 0
    for values in combinations_with_replacement(range(4), 3):
        for a in range(5):
            for b in range(5-a):
                old = list(zip(values, (F(a, 4), F(b, 4), F(4-a-b, 4))))
                expectation = sum(value*mass for value, mass in old)
                half_tail = tail_integral(old, F(1, 2))
                for q in levels:
                    w = min(q, 1-q)
                    scaled = [(value, w*mass) for value, mass in old]
                    for middle_value, target in ((3, expectation), (0, half_tail)):
                        padded = scaled + [(0, q-w), (middle_value, w/2), (3, 1-q-w/2)]
                        assert tail_integral(padded, q) == w*target
                        checked += 1
    print(f"{checked} exact common-level padding checks with ties and zero masses")


def check_binary_emissions():
    checked = 0
    for maximum in range(1, 8):
        for rewards in product(range(maximum+1), repeat=4):
            thresholds = [F(reward, maximum) for reward in rewards]
            breaks = sorted({F(0), F(1), *thresholds})
            outcomes = [(hi-lo, [int(hi <= threshold) for threshold in thresholds])
                        for lo, hi in zip(breaks, breaks[1:])]
            assert len(outcomes) <= len(rewards)+1
            assert sum(mass for mass, _ in outcomes) == 1
            means = [sum(mass*bits[j] for mass, bits in outcomes)
                     for j in range(len(rewards))]
            assert means == thresholds
            checked += 1
    print(f"{checked} exact binary-emission marginal vectors")


def check_hinge_identity():
    checked = 0
    for a, b, c in combinations_with_replacement(range(-2, 4), 3):
        for u in range(5):
            for v in range(5-u):
                atoms = [(a, F(u, 4)), (b, F(v, 4)), (c, F(4-u-v, 4))]
                for level in (F(1, 7), F(1, 4), F(1, 2), F(3, 4), F(6, 7)):
                    hinge = max(level*t-sum(mass*max(0, t-x) for x, mass in atoms)
                                for t in (a, b, c))
                    assert hinge == tail_integral(atoms, level)
                    checked += 1
    print(f"{checked} exact weighted hinge identities with signed payoffs and ties")


if __name__ == "__main__":
    check_multiplication()
    check_common_tail_levels()
    check_binary_emissions()
    check_hinge_identity()
