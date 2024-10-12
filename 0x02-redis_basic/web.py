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
        clinet.set(f"cached:{url}", 0)
        clinet.incr(f"count:{url}")
        clinet.setex(f"cached:{url}", 10, clinet.get(f"cached:{url}"))
        return method(url)
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    get_page
    """
    return requests.get(url).text


if __name__ == "__main__":
    get_page("https://google.com")
