#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio
import random


async def async_generator():
    """loop 10 times, return random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
