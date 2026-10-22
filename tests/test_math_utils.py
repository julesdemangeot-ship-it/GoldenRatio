"""Tests for math_utils module."""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from math_utils import golden_ratio


GOLDEN_RATIO_KNOWN = 1.618033988749895
TOLERANCE = 1e-12


def test_golden_ratio_value():
    """Result must match the known constant within tolerance 1e-12."""
    phi = golden_ratio()
    assert abs(phi - GOLDEN_RATIO_KNOWN) < TOLERANCE, (
        f"Expected φ ≈ {GOLDEN_RATIO_KNOWN}, got {phi}"
    )


def test_golden_ratio_algebraic_identity():
    """φ satisfies the identity φ² = φ + 1."""
    phi = golden_ratio()
    assert abs(phi ** 2 - (phi + 1)) < TOLERANCE, (
        f"Identity φ² = φ + 1 failed: φ²={phi**2}, φ+1={phi+1}"
    )


def test_golden_ratio_conjugate():
    """1/φ = φ - 1 (the conjugate relation)."""
    phi = golden_ratio()
    assert abs(1 / phi - (phi - 1)) < TOLERANCE, (
        f"Conjugate relation 1/φ = φ - 1 failed"
    )


def test_golden_ratio_is_float():
    """Return type must be float."""
    phi = golden_ratio()
    assert isinstance(phi, float), f"Expected float, got {type(phi)}"


def test_golden_ratio_positive():
    """The golden ratio is a positive number."""
    phi = golden_ratio()
    assert phi > 0


if __name__ == "__main__":
    tests = [
        test_golden_ratio_value,
        test_golden_ratio_algebraic_identity,
        test_golden_ratio_conjugate,
        test_golden_ratio_is_float,
        test_golden_ratio_positive,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed.")
    sys.exit(0 if passed == len(tests) else 1)
