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
        if(client.get(f"count:{url}")):
            client.incr(f"count:{url}")
        else:
            client.setex(f"count:{url}", 10, 1)
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    get_page
    """
    return requests.get(url).text


if __name__ == "__main__":
    get_page("https://google.com")
