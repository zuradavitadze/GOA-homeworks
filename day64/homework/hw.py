
class Car:
    """
    მანქანის კლასი, რომელსაც აქვს ბრენდი, მოდელი და გამოშვების წელი.
    """
    def __init__(self, brand, model, year):
        """
        მანქანის ობიექტის ინიციალიზაცია.

        Args:
            brand (str): მანქანის ბრენდი.
            model (str): მანქანის მოდელი.
            year (int): მანქანის გამოშვების წელი.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        """
        ბეჭდავს მანქანის სრულ ინფორმაციას.
        """
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}")


        class Student:
    """
    სტუდენტის კლასი, რომელსაც აქვს სახელი, ასაკი და შეფასება.
    """
    def __init__(self, name, age, grade):
        """
        სტუდენტის ობიექტის ინიციალიზაცია.

        Args:
            name (str): სტუდენტის სახელი.
            age (int): სტუდენტის ასაკი.
            grade (int): სტუდენტის შეფასება.
        """
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        """
        ამოწმებს, არის თუ არა სტუდენტი გადასული შემდეგ კლასში.

        Returns:
            bool: True, თუ შეფასება მეტია 5-ზე, False წინააღმდეგ შემთხვევაში.
        """
        return self.grade > 5


class Dog:
    """
    ძაღლის კლასი, რომელსაც აქვს სახელი და ასაკი.
    """
    def __init__(self, name, age):
        """
        ძაღლის ობიექტის ინიციალიზაცია.

        Args:
            name (str): ძაღლის სახელი.
            age (int): ძაღლის ასაკი.
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        ბეჭდავს "Woof!".
        """
        print("Woof!")