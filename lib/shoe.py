#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    # def get_title(self):
    #     return self._title

    # def set_title(self, title):
    #     self._title = title

    # title = property(get_title, set_title)

    # def set_page_count(self, page_count):
    #     if isinstance(page_count, int):
    #         self._page_count = page_count
    #     else:
    #         print("page_count must be an integer")

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        setattr(self, "condition", "New")

    pass

shoe = Shoe("Ford", 12)
shoe.cobble()