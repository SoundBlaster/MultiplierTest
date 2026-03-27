"""Core multiplication helpers for the project."""

from __future__ import annotations

from typing import Protocol, TypeVar


T = TypeVar("T")


class SupportsMul(Protocol[T]):
    """Protocol describing values that can be multiplied by their own type."""

    def __mul__(self, other: T, /) -> T:
        """Return the product with ``other``."""


def multiply(a: SupportsMul[T], b: T) -> T:
    """Return the product of two multiplicative values.

    The function is generic and works with any pair of values where ``a * b``
    is valid and returns the same result type.
    """
    return a * b
