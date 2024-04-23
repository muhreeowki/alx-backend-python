#!/usr/bin/env python3
"""Task 1 Module"""

import asyncio
from typing import List
from importlib import import_module as using

async_generator = using("./0-async_generator.py").async_generator


async def async_comprehension() -> List[float]:
    """Task 1 Function"""
    return [num async for num in async_generator()]
