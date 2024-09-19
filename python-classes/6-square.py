#!/usr/bin/python3


class Square():
    """_summary_
    """
    def __init__(self, size = 0, position=(0, 0)) -> None:
            self.__size = size
            self.__position = position
    
    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not type(value) is int :
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        all_positive = all(x > 0 for x in value)
        if not type(value) is tuple or not len(value) is 2 or not all_positive:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def area(self):
        return (self.__size ** 2)
    
    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            for index in range(0, self.__size):
                for index2 in range(0, self.__position[0]):
                    print(" ", end="")
                    index2 += 1
                for index3 in range(0, self.__size):
                    print("#", end="")
                    index3 += 1
                print("")
                index += 1





        

        

        
    
        
