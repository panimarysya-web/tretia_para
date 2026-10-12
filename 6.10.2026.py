# print("Обработка исключений")
#
# def set_age(age):
#     if age < 0:
#         raise ValueError("out of range")
#
# import logging
# except ConnectionError as e:
#     logging.error("Ошибка сети")
#     raise ConnectionError("Ошибка сети")
#
# except ConnectionError:
#     logging.error("Ошибка сети")
#     raise ConnectionError


#
# class BaseParser:
#     def parse(self, data):
#         raise NotImplementedError(f"Класс {self.__class__.__name__} должен реализовывать метод parse")

#
# import json             # перевод в джейсон формат...
# data = {"name" : "Иван",
#         "is_student" : True,
#         "grades" : [4,5,5]}
# json_str = json.dumps(data, ensure_ascii=False) #второй параметр задает кодировку, чтобы русские буквы оставались неизмены
# print(json_str)
#
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
# with open("data.json", "r", encoding="utf-8") as f:
#     loaded_data = json.load(f)
# print(loaded_data)



import json
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# stud = Student("Петр", 19)
def student_to_dict(obj):
    if isinstance(obj, Student):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Unknown object type")
# json_str = json.dumps(stud, default=student_to_dict, ensure_ascii=False)
# with open ("data_2.json", "w", encoding='utf-8') as f:
#     json.dump(json_str, f, ensure_ascii=False, indent=4)
with open ("students_db.json", "r", encoding='utf-8') as f:
    students = json.load(f)
for student in students:
    if student["is_active"]:
        print(student["name"])
for student in students:
    if not student["is_active"]:
        student["scholarship"] = 0
with open ("students_updated.json", "w", encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)



