#!/usr/bin/env python3
"""an asynchronous coroutine"""
from typing import List
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """using tasks"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    task_list = []
    for i in range(n):
        task_list.append(asyncio.create_task(wait_random(max_delay)))

    results = await asyncio.gather(*task_list)
    return sorted(results)
