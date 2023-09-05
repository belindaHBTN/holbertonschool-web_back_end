#!/usr/bin/env python3
"""a Python func that changes all topics of a document based on the name"""

def update_topics(mongo_collection, name, topics):
    """update topics"""
    mongo_collection.update_one({"name":name}, {"$set": {"topics":topics}})
