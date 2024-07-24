#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
You can overload def __init__(self): but don’t
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data
the item value for the key key.
If key or item is None, this method should not
do anything.
If the number of items in self.cache_data is

