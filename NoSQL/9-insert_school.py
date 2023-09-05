#!/usr/bin/env python3
"""a Python function that inserts a new document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """insert a new document and return its id"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
