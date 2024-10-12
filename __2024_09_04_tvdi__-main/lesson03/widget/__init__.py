
#自訂常數

MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6
SUN = 7

#自訂 class
class Person(object):
    #自訂的init,建立內建的attribute
    def __init__(self,name:str,age:int): #type hint
        self.__name = name #private attribute
        self.__age = age #private attribute

    #自訂實體被print()時的輸出
    def __repr__(self)->str:
        return f'我的名字是:{self.name}\n我的age是{self.age}'
    
    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self,n):
        print(f"不可以改名為{n}")

    @property
    def age(self)->int: #getter
        return self.__age
    
    @age.setter
    def age(self,value): #setter
        if value > 100 or value < 0:
            print("不合法的值")
        else:
            self.__age = value


class Student(Person):   #繼承Person
    @classmethod
    def echo(cls):
        print("Hello! I am a StudentClass")

    def __init__(self, name: str, age: int,chinese:int=0, english:int=0, math:int=0): #可以寫入預設值
        super().__init__(name, age) 
        self.chinese=chinese
        self.english =english
        self.math = math

    @property
    def total(self)->int:
        return self.chinese + self.english +self.math
    
    #instance method 實體方法
    #代表要用 實體 stu1 來執行 (要加括號，因為是一個方法)
    def average(self)->float:
        return round(self.total/3,2)






#自訂FUNCTION

def get_person(name:str,age:int)->Person:
    return Person(name,age)



def get_student(name1:str,age1:int,chinese=60,english=60,math=60)->Student:
    return Student(name=name1,age=age1,chinese=chinese,english=english,math=math)

