#!/usr/bin/env python3
"""
Show Stats of Collection
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """
    Show Stats of Collection
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    all_collections_count = nginx_collection.count_documents({})

    print(f"{all_collections_count} logs")

    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    get_and_status = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{get_and_status} status check")
