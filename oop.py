# -----------------------------
# Assignment 1: Design Your Own Class – Book
# -----------------------------

# Base Class: Book
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def show_info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}")

    def read_pages(self, number):
        if number <= self.pages:
            print(f"You read {number} pages of '{self.title}'. Enjoy!")
        else:
            print(f"'{self.title}' only has {self.pages} pages!")

# Subclass: EBook inherits Book
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size  # in MB

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB)... Done!")

# -----------------------------
# Creating Book Objects
# -----------------------------
book1 = Book("The Alchemist", "Paulo Coelho", 208, "Fiction")
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, "Thriller", 2.5)

print("\n--- Book Info ---")
book1.show_info()
book1.read_pages(50)

ebook1.show_info()
ebook1.download()
ebook1.read_pages(100)

# -----------------------------
# Assignment 2: Design Your Own Class – Superhero
# -----------------------------

# Base Class: Superhero
class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city

    def show_identity(self):
        print(f"Hero: {self.name} from {self.city}")

    def use_power(self):
        print(f"{self.name} uses {self.superpower}!")

# Subclass: FlyingHero inherits Superhero
class FlyingHero(Superhero):
    def __init__(self, name, superpower, city, flight_speed):
        super().__init__(name, superpower, city)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

# -----------------------------
# Creating Superhero Objects
# -----------------------------
hero1 = Superhero("Shadow", "Invisibility", "Gotham")
hero2 = FlyingHero("Skyhawk", "Wind Manipulation", "Metropolis", 300)

print("\n--- Superhero Info ---")
hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()
hero2.fly()

# -----------------------------
# Assignment 3: Polymorphism Challenge – Animals & Vehicles
# -----------------------------

# Base Classes
class Vehicle:
    def move(self):
        pass

class Animal:
    def move(self):
        pass

# Vehicles
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water 🚤")

# Animals
class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Polymorphism in Action
vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Bird(), Fish()]

print("\n--- Vehicles Moving ---")
for v in vehicles:
    v.move()

print("\n--- Animals Moving ---")
for a in animals:
    a.move()
