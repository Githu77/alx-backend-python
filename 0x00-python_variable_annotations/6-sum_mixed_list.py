#!/usr/bin/env python3
'''
Module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Sums up a list of integers and floating-point No.s.
    '''
    return float(sum(mxd_lst))
