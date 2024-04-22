#!/usr/bin/env python3
"""Task 0"""

import random
import asyncio


async def wait_random(max_delay=10.0):
    """Function that waits a random amount of time"""
    duration = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
