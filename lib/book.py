class Book:
    def __init__(self, title, page_count=50):
        self.title = title
        self.page_count = page_count

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    title = property(get_title, set_title)

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    page_count = property(get_page_count, set_page_count)

    # this part of the code is complete bullshit and they need to fix it. It should say explicitly print not output
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")

    

The_Hobbit = Book("The Hobbit", 1000)
print(The_Hobbit.title, The_Hobbit.page_count)

result = The_Hobbit.turn_page()
print(result)  


