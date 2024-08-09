#!/usr/bin/env python3
"""Task 1"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay."""
    wait = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait)
