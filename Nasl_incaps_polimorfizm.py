# задание 1

# import random
#
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist=[]):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def play_random_track(self):
#
#         if not self.tracklist:
#             print("Треклист пуст")
#         else:
#             random_track = random.choice(self.tracklist)
#             print(f"Воспроизводится случайный трек: {random_track}")
#
#
# album1 = MusicAlbum("Album Title", "Artist Name", 2022, "Genre", ["Track 1", "Track 2", "Track 3"])
#
# album1.play_random_track()






# задание 2

# class Student:
#     def __init__(self, name, age, grade, scores=[]):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def average_score(self):
#
#         if not self.scores:
#             return 0
#         return sum(self.scores) / len(self.scores)
#
# student2 = Student("Саетгареев Самат", 16, "9А", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())



# задание 3

# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print(f"Продукты для рецепта '{self.name}':")
#         for ingredient in self.ingredients:
#             print(f"- {ingredient}")
#
#     def cook(self):
#         print(f"Готовим блюдо по рецепту '{self.name}'...")
#         print(f"{self.name} готово! Приятного аппетита!")
#
# recipe1 = Recipe("Паста", ["Макароны", "Фарш", "Помидоры", "Лук", "Чеснок"])
# recipe1.print_ingredients()
# recipe1.cook()




# задание 4


# class Publisher:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         print(f"Издательство: {self.name}, Расположение: {self.location}")
#
#     def publish(self, message):
#         print(f"Издание: {message} находится в печати.")
#
# class BookPublisher(Publisher):
#     def __init__(self, name, location, num_authors):
#         super().__init__(name, location)
#         self.num_authors = num_authors
#
# class NewspaperPublisher(Publisher):
#     def __init__(self, name, location, num_pages):
#         super().__init__(name, location)
#         self.num_pages = num_pages
#
# book_publisher = BookPublisher("Книжное Издательство", "Город", 10)
# book_publisher.get_info()
# book_publisher.publish("Новая книга")
#
# newspaper_publisher = NewspaperPublisher("Газетное Издательство", "Город", 20)
# newspaper_publisher.get_info()
# newspaper_publisher.publish("Новый выпуск газеты")



# задание 5


# class BankAccount:
#     def __init__(self, balance=0, interest_rate=0.01):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f"Депозит: +{amount}")
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"Снятие: -{amount}")
#         else:
#             print("Недостаточно средств на счете.")
#
#     def add_interest(self):
#         interest = self.__balance * self.__interest_rate
#         self.__balance += interest
#         self.__transactions.append(f"Начисление процентов: +{interest}")
#
#     def history(self):
#         print("История операций:")
#         for transaction in self.__transactions:
#             print(transaction)
#
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(200)
# account.add_interest()
# account.history()




# задание 6

# class Employee:
#     def __init__(self, name, age, salary, bonus=0):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#         self.__bonus = bonus
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
# employee = Employee("Самат", 30, 50000)
# print(f"Имя: {employee.get_name()}")
# print(f"Возраст: {employee.get_age()}")
# print(f"Оклад: {employee.get_salary()}")
# employee.set_bonus(2000)
# print(f"Бонус: {employee.get_bonus()}")
# print(f"Общая зарплата: {employee.get_total_salary()}")



# задание 7

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f"{self.name} издает звук.")
#
#     def move(self):
#         print(f"{self.name} двигается.")
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species="Собака", legs=4)
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.name} лает.")
#
# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name, species="Птица", legs=2)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f"{self.name} летит.")
#
# dog = Dog("Шарик", "Дворняга")
# dog.voice()
# dog.move()
# dog.bark()
#
# bird = Bird("Чижик", wingspan=30)
# bird.voice()
# bird.move()
# bird.fly()



# задание 8

# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def describe(self):
#         print(f"{self.color} {self.name}")
#
# class Circle(Shape):
#     def __init__(self, name, color, radius):
#         super().__init__(name, color)
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, name, color, length, width):
#         super().__init__(name, color)
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Triangle(Shape):
#     def __init__(self, name, color, base, height):
#         super().__init__(name, color)
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# circle = Circle("Круг", "Красный", 5)
# circle.describe()
# print(f"Площадь: {circle.area()}")
#
# rectangle = Rectangle("Прямоугольник", "Синий", 4, 6)
# rectangle.describe()
# print(f"Площадь: {rectangle.area()}")
#
# triangle = Triangle("Треугольник", "Зеленый", 3, 8)
# triangle.describe()
# print(f"Площадь: {triangle.area()}")




# задание 10
# class Soldier:
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self._rank = rank
#         self._service_number = service_number
#
#     def get_rank(self):
#         return self._rank
#
#     def confirm_service_number(self, number):
#         return self._service_number == number
#
#     def promote(self):
#         pass
#
#     def demote(self):
#         pass
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
# print(soldier1.get_rank())
# soldier1.promote()
# soldier1.demote()

