# Python Classes Assignment README

## Overview

This assignment demonstrates the following concepts in Python:

1. **Class Design and Constructors**: Creating classes like `Book`, `EBook`, `Superhero`, and `FlyingHero` with unique attributes.
2. **Inheritance**: Subclasses inherit properties and methods from parent classes (`EBook` inherits `Book`, `FlyingHero` inherits `Superhero`).
3. **Encapsulation**: Attributes are initialized inside classes and accessed or modified through methods.
4. **Polymorphism**: Different classes implement the same method (`move()`) differently to show polymorphic behavior.
5. **Humanized Output**: Friendly, readable print statements to make the program interactive and user-friendly.

## File Structure

* `assignment.py`: Main Python program containing all classes and examples.
* `README.md`: This file explaining the assignment.

## Features Demonstrated

### 1. Book Classes

* **Book**: Represents a book with title, author, pages, and genre.
* **EBook**: Inherits from Book and adds file size; includes a method to download the ebook.

### 2. Superhero Classes

* **Superhero**: Represents a superhero with name, superpower, and city.
* **FlyingHero**: Inherits from Superhero and adds flight speed; includes a method to fly.

### 3. Polymorphism Challenge

* **Vehicles**: `Car`, `Plane`, `Boat` all implement `move()` differently.
* **Animals**: `Dog`, `Bird`, `Fish` all implement `move()` differently.

## How to Run

1. Ensure you have Python 3.x installed.
2. Open a terminal or IDE.
3. Run the program using:

```
python assignment.py
```

4. Observe the outputs demonstrating class behavior, inheritance, and polymorphism.

## Notes

* Constructors initialize each object with unique values.
* Methods simulate real-world behavior (reading pages, using powers, moving vehicles and animals).
* This assignment is fully humanized with friendly print statements to make it easy to understand.

---

**Author:** Henok Girma
**Course:** Python Programming
**Assignment:** Design Your Own Class & Polymorphism Challenge
