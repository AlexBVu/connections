import sys

class Book:
        contact_book = {}
        
        def __init__(self, initial_person: str, time: int) -> None:
                if type(initial_person) != str or type(time) != int:
                        sys.exit()
                contact_book = {}

                contact_book[initial_person] = time


        def add_person(self, name: str, time: int) -> None:
                if type(name) != str or type(time) != int:
                        sys.exit()

                contact_book[name] = time

                