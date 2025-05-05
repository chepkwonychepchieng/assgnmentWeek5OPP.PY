
# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")
        print(f"This book has {self.pages} pages.") 

class story_book(book):
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author, pages)
        self.genre = genre

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")
        print(f"This is a {self.genre} book with {self.pages} pages.")

my_book = book("Building Capacity", "Emmanuel Favour", 180)
my_book.read()
my_story_book = story_book("the river and the source", "Margaret Ogolla", 280, "fiction")
my_story_book.read()


# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class bus:
    def move(self):
        return "Bus moves by driving  "
    
class car:
    def move(self):
        return "Car moves by driving  "  
    
class bike:
    def move(self):
        return "Bike moves by pedaling  "
    
for vehicle in [bus(), car(), bike()]:
    print(vehicle.move())
