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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store - generet uuid as a key and store it
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, data: bytes) -> str:
        """
        get_str - decode utf8 bytes
        """
        if not data:
            return None
        return data.decode('utf8')

    def get_int(self, data: bytes) -> int:
        """
        get_int - return int from bytes
        """
        if not data:
            return None
        return int(self.get_str(data))

    def get(self, key: str, fn: callable = get_str) -> str:
        """
        get - get data by key
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
