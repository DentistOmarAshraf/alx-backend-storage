#!/usr/bin/env python3
"""
Cache - redis exercise
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count_calls - method store function call in redis
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history - method store input and output of methods
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        method_return = method(self, *args, **kwargs)
        self._redis.rpush(output_key, method_return)
        return method_return
    return wrapper


def replay(method: Callable) -> None:
    """
    Print info from redis about method
    """
    client = redis.Redis()
    m_name = method.__qualname__
    in_list = client.lrange(f"{m_name}:inputs", 0, -1)
    out_list = client.lrange(f"{m_name}:outputs", 0, -1)
    combination = list(zip(in_list, out_list))
    print(f"{m_name} was called {client.get(m_name).decode('utf8')} times:")
    for input, output in combination:
        print(f"{m_name}(*{input.decode('utf8')}) -> {output.decode('utf8')}")


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

    @count_calls
    @call_history
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

    def get(self, key: str, fn: callable = None) -> str:
        """
        get - get data by key
        """
        data = self._redis.get(key)
        if fn and data:
            return fn(data)
        return data
