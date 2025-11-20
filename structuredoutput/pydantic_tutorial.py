from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name : str = 'nadin' #passing default values
    age : Optional[int] = None #setting optional values
    email : EmailStr
new_student = {'age':22,'email':'nadintamang10@gmail.com'}
student = Student(**new_student)

print(student)
print(type(student))