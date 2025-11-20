#we will be using with_structured_output
from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int

new_person: Person = {'name':'nadin','age':35}
print(new_person)
print(type(new_person))