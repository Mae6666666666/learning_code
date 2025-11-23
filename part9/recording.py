

class Recording:
    __length = 0
    def __init__(self, length_temp):
        self.__length = length_temp

    def __str__(self):
        return self.__length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, taking_length: int):

        if taking_length <= 0:
            raise ValueError("taking_length must be a positive integer")
        else:
            self.__length = taking_length



the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)
