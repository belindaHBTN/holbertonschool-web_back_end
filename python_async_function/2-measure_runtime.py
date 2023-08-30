#!/usr/bin/env python3
"""measures the total execution time"""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n:int, max_delay:int) -> float:
    """measure time function"""
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
