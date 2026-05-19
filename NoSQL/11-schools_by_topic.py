#!/usr/bin/env python3
"""
this comment is for something
"""


def schools_by_topic(mongo_collection, topic):
    """ 
    this one too
    """
    return mongo_collection.find({"topic": topic})
