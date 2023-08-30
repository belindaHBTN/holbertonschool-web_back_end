#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel"""
    async_comprehension = __import__(
            '1-async_comprehension').async_comprehension

    start_time = asyncio.get_event_loop().time()

    task_list = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task_list)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
