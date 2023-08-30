#!/usr/bin/env python3
"""an asynchronous coroutine"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time"""
    delay_list = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
