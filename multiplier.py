"""Core multiplication helpers for the project."""

from __future__ import annotations

from numbers import Number
from typing import TypeVar, cast


NumberT = TypeVar("NumberT", bound=Number)


def multiply(a: NumberT, b: NumberT) -> NumberT:
    """Return the product of two numeric values."""
    return cast(NumberT, a * b)
