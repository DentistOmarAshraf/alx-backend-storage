#!/usr/bin/env python3
"""
list_all - function return all document in collection
pymongo
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    mongo_collection: type client.collection
    return: list of all document in collection
    """
    data = mongo_collection.find()
    return data
