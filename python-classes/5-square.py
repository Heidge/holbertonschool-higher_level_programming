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
        self.__size = size

    @property
    def size(self):
        """Retrieves size value

        Returns:
            Integer: size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Allows to set a new value to size field

        Args:
            value (integer): the value which will be set

        Raises:
            TypeError: if the value is not of type int
            ValueError: if value is less than 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method for retrieves the area of the square object

        Returns:
            Integer: area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method for print a representation of the square
        """
        if self.__size == 0:
            print("\n")
        else:
            for index in range(0, self.__size):
                for index2 in range(0, self.__size):
                    print("#", end="")
                    index2 += 1
                print("")
                index += 1
