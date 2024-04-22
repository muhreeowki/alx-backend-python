#!/usr/bin/env python3
"""Task 1"""

import random
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay=10.0):
    """Function that waits a random amount of time"""
    durations = []
    for _ in range(n):
        duration = random.uniform(0, max_delay)
        await asyncio.sleep(duration)
        durations.append(duration)
    return durations
