#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if isinstance(size, int):
                raise TypeError("size must be an integer")
        except (TypeError):
            print("size must be an integer")
        self.__size = size
        # except (ValueError):
        #     print("size must be >= 0")
        # if isinstance(size, int):
        #     raise TypeError("size must be an integer")
        # if size < 0:
        #     raise ValueError("size must be >= 0")
        # else:  self.__size = size
        # if isinstance(size, int):
        #     raise TypeError("size must be an integer")
        # elif size < 0:
        #     raise ValueError("size must be >= 0")
        # else:
        #     self.__size = size

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)