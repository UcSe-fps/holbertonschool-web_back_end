#!/usr/bin/env python3
import pymongo


def list_all(mongo_collection):
    """this will give all the documents in the db"""

    return list(mongo_collection.find())
