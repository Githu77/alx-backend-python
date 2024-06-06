#!/usr/bin/env python3
'''
Module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Multiplier function.
    '''
    return lambda x: x * multiplier
