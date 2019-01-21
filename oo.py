"""
1. Discussion
-------------

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   (1)Abstraction: users are able to hide details they don't need
   (2)Encapsulation: data and methods are kept together
   (3)Polymorphism: interchangeability of components

2. What is a class?
    A class is a type of thing, like string, file, list or dictionary

3. What is a method?
    A method is a function defined on a class.

4. What is an instance in object orientation?
    An instance is an individuaal occurrence of a class

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   The class attribute is a piece of data on the class itself. When this is asked on an instance, it can be found on the class. An instance attribute is set directly on the object.


"""


# 2. Road Class
# #############################################################################

# Create your Road class here
class Road:
    num_lanes = 2
    speed_limit = 25

# Instantiate Road objects here
# road_1 = Road()
# road_2 = Road()
# road_1.num_lanes = 4
# road_1.speed_limit = 60




# 3. Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here
    def update_password(self, current_password, new_password):
        if current_password != self.password:
            print("Invalid password")
        else:
            self.password = new_password



# 4. Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here
class Library:
    def __init__(self, books):
        self.books = books


    def add_bood(self, title, author):
#how to instantiate a book object and add it to the library's books list??
    def find_books_by_author(self, author):
        if self.author in self.books:
            return self.books ??

