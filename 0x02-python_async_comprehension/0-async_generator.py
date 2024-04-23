#!/usr/bin/env python3
"""Task 0 module"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Task 0 coroutine"""
    nums = []
    for i in range(10):
        await asyncio.sleep(1)
        nums.append(random.uniform(0, 10))
    return nums
