#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay=10):
    random_time = random.uniform(0, max_delay)
    await asyncio.sleep(random_time)
    return random_time
