#!/usr/bin/env python3
"""a Python script that provides stats about Nginx logs"""
from pymongo import MongoClient


def nginx_stats(collection):
    """display some stats about Nginx logs stored in MongoDB"""
    logs = collection.count_documents({})
    print(f'{logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    tab = '\t'
    print('Methods:')
    for method in methods:
        print(f'{tab}method {method}: {collection.count_documents({"method":method})}')

    status = collection.count_documents({"method":"GET", "path":"/status"}) 
    print(f'{status} status check')


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    nginx_stats(nginx_collection)

