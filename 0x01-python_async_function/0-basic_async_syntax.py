#!/usr/bin/env python3
import random
import time


async def wait_random(max_delay=10.0):
    duration = random.uniform(0, max_delay)
    time.sleep(duration)
    return duration
