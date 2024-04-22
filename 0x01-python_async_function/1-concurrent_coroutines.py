#!/usr/bin/env python3
import random
import time

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay=10.0):
    durations = []
    for _ in range(n):
        duration = random.uniform(0, max_delay)
        time.sleep(duration)
        durations.append(duration)
    return durations
