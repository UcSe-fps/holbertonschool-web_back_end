#!/usr/bin/env python3


def update_topics(mongo_collection, name, topics):
    """ 
        this will be something
    """
    return mongo_collection.update_many({"name": name},
{$set: {"topics": topics}})
