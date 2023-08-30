#!/usr/bin/env python3
"""an asynchronous coroutine"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """execute multiple coroutines at the same time"""
    delay_list = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return delay_list
