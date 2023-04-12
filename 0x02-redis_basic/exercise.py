#!/usr/bin/env python3
"""
Writing strings to Redis
"""


import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """
    Create a Cache class.
    In the __init__ method, store an instance of the Redis client as
    a private variable named _redis (using redis.Redis())
    and flush the instance using flushdb.

    Create a store method that takes a data argument and returns a string.
    The method should generate a random key (e.g. using uuid),
    store the input data in Redis using the random key and return the key.

    Type-annotate store correctly.
    Remember that data can be a str, bytes, int or float.
    """

    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                   bytes,
                                                                   int,
                                                                   float]:
        """Get data from Redis."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get data from Redis as a string."""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get data from Redis as an int."""
        return self.get(key, int)

