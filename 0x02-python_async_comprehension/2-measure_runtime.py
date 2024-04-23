#!/usr/bin/env python3
"""Task 2 Module"""

import asyncio
from typing import List
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """Task 2 Function"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
