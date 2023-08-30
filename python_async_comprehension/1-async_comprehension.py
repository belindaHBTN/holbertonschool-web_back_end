#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """return the list of numbers"""
    async_generator = __import__('0-async_generator').async_generator

    num_list = [number async for number in async_generator()]
    return num_list
