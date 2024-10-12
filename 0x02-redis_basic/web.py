#!/usr/bin/env python3
"""
Web.py
"""
import requests
import redis
from functools import wraps
from typing import Callable

clinet = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
    count_url
    """
    @wraps(method)
    def wrapper(url):
        if clinet.ttl(url) <= -1:
            clinet.setex(f"count:{url}", 10, 0)
        else:
            clinet.incr(f"count:{url}")
        return method(url)
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    get_page
    """
    return requests(url).text
