#!/usr/bin/env python3
"""This is a module  for creating an asynchronous generator."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This coroutine asynchronously yields random floats."""
    n: int = 1
    while n <= 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        n += 1