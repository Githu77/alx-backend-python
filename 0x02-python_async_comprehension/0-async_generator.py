#!/usr/bin/env python3
'''
Module 0.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Generates 10 No.s.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
