# 0x0C. Python - Almost a circle

This project models a Rectangle and an Square. This class have a methods that permit,  create and save all created objects in a json file Rectangle.json and Square.json respectiely. Also you can read this files and create the objects.

## Examples:

- Save objects in json file

    ```python

    from models.rectangle import Rectangle

    r1 = Rectangle(2, 3)
    print(r1)
    r1.display()

    r2 = Rectangle(4, 6, 2, 3)
    print(r2)
    r2.display()

    list_rectangles = [r1, r2]
    Rectangle.save_to_file(list_rectangles)

    ```

- Load objects from json files

    ```python

    from models.square import Squre

    list_squares = Square.load_from_file()

    for s in list_square:
        print(s)
        s.display()

    ```

---
## Resources:books:
Read or watch:
* [args/kwargs](https://alx-intranet.hbtn.io/rltoken/7gc6UzxSL81HcuAwklUbuQ)
* [JSON encoder and decoder](https://alx-intranet.hbtn.io/rltoken/rGVU9mt57rVURGnjK6n4_Q)
* [unittest module](https://alx-intranet.hbtn.io/rltoken/soictNXCPE18ASL3INoeew)
* [Python test cheatsheet](https://alx-intranet.hbtn.io/rltoken/uI9iskBCcNo5pc7j9Vy86A)

---
## Learning Objectives:bulb:
What I learned from this project:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---
## Files

### Models:(./models)
* [**Base:**](./models/base.py) Class to structure any geometry class. 
* [**Rectangle:**](./models/rectangle.py) Class to model a Rectangle object.
* [**Square:**](./models/square.py) Class to model a Square object.

### [Test:](./tests/)
* [**test_base:**](./tests/tests_base.py)
* [**test_rectangle:**](./tests/tests_rectangle.py)
* [**test_square:**](./tests/tests_square.py)

---

## Author
* **Chacha Alex Chacha** - [Chacha-A-Chacha](https://github.com/Chacha-A-Chacha)