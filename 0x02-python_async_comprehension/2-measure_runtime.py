#!/usr/bin/env python3
"""The coroutine that will execute async_comprehension four times in
parallel using asyncio.gather"""


import asyncio
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = asyncio.get_event_loop().time() - start_time
    return total_time