#!/usr/bin/python3
"""
Module for create a square object.
Will contains every attributes.
"""


class Square():
    """
    Class for create square object
    """
    def __init__(self, size=0) -> None:
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
