#!/usr/bin/env python3
"""Task 0 module"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Task 0 coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
