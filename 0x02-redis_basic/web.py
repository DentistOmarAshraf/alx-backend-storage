#!/usr/bin/env python3
"""
Web.py
"""
import requests
import redis
from functools import wraps
from typing import Callable

client = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
    count_url
    """
    @wraps(method)
    def wrapper(url):
        client.incr(f'count:{url}')
        result = client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        client.set(f'count:{url}', 0)
        client.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    get_page
    """
    return requests.get(url).text


if __name__ == "__main__":
    get_page("https://google.com")
