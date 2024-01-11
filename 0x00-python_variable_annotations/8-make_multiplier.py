#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that
    returns a function that multiplies the float"""
    return lambda x: x * multiplier
