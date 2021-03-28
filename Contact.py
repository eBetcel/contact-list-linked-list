class Contact:
    def __init__ (self, number, name):
        self._number = number
        self.__name = name

    @property
    def name(self):
        return self.__name
    