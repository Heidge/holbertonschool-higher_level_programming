#!/usr/bin/python3


class Square():
    
    def __init__(self, size = 0) -> None:
            self.__size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        return (self.__size ** 2)
    
    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            for index in range(0, self.__size):
                for index2 in range(0, self.__size):
                    print("#", end="")
                    index2 += 1
                print("")
                index += 1





        

        

        
    
        
