#!/usr/bin/env python3
"""
insert_school - function insert document into collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection: collection inside database
    kwargs: key, value argements
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
