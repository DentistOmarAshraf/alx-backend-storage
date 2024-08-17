#!/usr/bin/env python3
"""
Query Db collection by filter
"""


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection - collection
    topic - value to search
    """
    data = mongo_collection.find({'topics': topic})
    return data
