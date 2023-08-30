#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return a async task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
