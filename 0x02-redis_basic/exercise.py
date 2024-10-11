#!/usr/bin/env python3
"""
Cache - redis exercise
"""
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache - redis exercise
    """

    def __init__(self):
        """
        init - initialize instance of redis and flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        """
        store - generet uuid as a key and store it
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
