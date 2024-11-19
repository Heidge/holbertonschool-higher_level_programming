#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, item, counter=0):
        self.item = iter(item)
        self.item_length = len(item)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        if self.counter < self.item_length :
            self.counter += 1
            return next(self.item)
        else:
            raise StopIteration
