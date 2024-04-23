#!/usr/bin/env python3
"""Task 1 Module"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Task 1 Function"""
    return [num async for num in async_generator()]
