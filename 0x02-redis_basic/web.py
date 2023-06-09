#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

from typing import Callable
from functools import wraps


def count_requests(method: Callable) -> Callable:
    """
    Track how many times a url has been accessed
    """
    @wraps(method)
    def wrapper(self, url: str) -> str:
        """
        Wrapper function
        """
        self._redis.incr(f"count:{url}")
        return method(self, url)
    return wrapper
