#!/usr/bin/env python3
"""
update_topics - function update documents values
"""


def update_topics(mongo_collection, name, topics):
    """
    mongo_collection - dbs collection
    name: filter
    """
    mongo_collection.update_many(
            {"name": name},
            {'$set': {"name": name, "topics": topics}}
            )
