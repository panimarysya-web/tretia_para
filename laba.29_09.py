# Магические функции
import math


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # def __str__(self):
#     #     return f'{self.name} is {self.age} years old'
#     def __repr__(self):
#         return f'{self.name} is {self.age} years old'
# cat = Cat("John", 25)
# print(repr(cat))




# print("Это пример работы с декораторами")


# def my_shiny_new_decorator(function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает ДО вызова функции")
#         function_to_decorate()
#         print("А я - код, который отработает ПОСЛЕ")
#     return the_wrapper_around_the_original_function
# # def stand_alone_function():
# #     print("Я простая функция и я не хочу изменений")
# # stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# # stand_alone_function_decorated()
# @my_shiny_new_decorator
# def stand_alone_function2():
#     print("Я синтаксический сахар")
# stand_alone_function2()



# print("Делаем сендвичи")


# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print(" <\_____/>")
#     return wrapper
# def ingredients(func):
#     def wrapper():
#         print("  #######")
#         func()
#         print("  ~~~~~~~")
#     return wrapper
# @bread
# @ingredients
# def sandwich(food = "  -_-_-_-"):
#     print(food)
# # sandwich = bread(ingredients(sandwich))
# sandwich()


#
# print("еще один пример")
#
#
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я поолучил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
# print_full_name("Васисуалий", "Лоханкин")
#



# class MyClass:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
# class MathUtil:
#     @staticmethod
#     def add(a, b):
#         return a + b




# print("Пример еще один")
#
#
# class User :
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#     @staticmethod
#     def is_valid_age(age) :
#         return isinstance(age, int) and 0 <= age <= 100
#     @staticmethod
#     def is_valid_name(name) :
#         return isinstance(name, str) and len(name) > 0
#
# if User.is_valid_age(25) and User.is_valid_name("Васька") :
#     user = User('Васька', 25)
#     print(user.age, user.name)






#
# class Shape:
#     def area(self):
#         print("метод area должен быть определен")
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
# circle = Circle(10)
# circle.area()




# print("Это про абстрактные методы")
#
#
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     def describe(self):
#         print('я фигура площадью ', self.area())
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side * self.side
# sq = Square(10)
# print(sq.area())
# print(sq.describe())






from abc import ABC, abstractmethod
class DataProcessor(ABC):
    def __init__(self, data):
        self.data = data
    @abstractmethod
    def process(self):
        pass
    @staticmethod
    def valid_data(data):
        return isinstance(data, list) and len(data) > 0
    @staticmethod
    def format_output(result):
        return f"Результат: {result}"
class NumberProcessor(DataProcessor):
    def process(self):
        if not self.valid_data(self.data):
            print("Некорректные данные")
        return sum(self.data)
processor = NumberProcessor([1, 2, 3, 4, 5])
result = processor.process()
print(NumberProcessor.format_output(result))

