#!/usr/bin/env python3
'''
Module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Converts the key and its value to the tuple key and its square.
    '''
    return (k, float(v**2))
