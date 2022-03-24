#1
class Circle:
    def __init__(self,area=25,color="yellow"):
        self.__area=area
        self.__color=color

    def getArea(self):
        return self.__area

    def setArea(self,area):
        self.__area=area

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color=color

    def __str__(self):
        return str(self.__area)+" "+self.__color

circle1=Circle()
circle2=Circle(50)
print(circle1)
print(circle2)

class Square:
    def __init__(self,area=45,color="red"):
        self.__area = area
        self.__color = color

    def getArea(self):
        return self.__area

    def setArea(self, area):
        self.__area = area

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return str(self.__area) + " " + self.__color

square1=Square(60)
square2=Square(40,"pink")


print(square1)
print(square2)



#2

class Apartment:
    def __init__(self,add,house_num,price,rent_price):
        self.__add=add
        self.__house_num=house_num
        self.__price=price
        self.__rent_price=rent_price

    def getAdd(self):
        return self.__add

    def setAdd(self,add):
        self.__add = add

    def getHouseNum(self):
        return self.__house_num

    def setHouseNum(self,house_num):
        self.__house_num=house_num

    def getPrice(self):
        return self.__price

    def setPrice(self,price):
        self.__price=price

    def getRentPrice(self):
        return self.__rent_price

    def setRentPrice(self,rent_price):
        self.__rent_price=rent_price

    def tesuaa(self):
        return (((self.__rent_price*12)/self.__price)*100)


    def __str__(self):
        return self.__add+" "+str(self.__house_num)+" "+str(self.__price)+" "+str(self.__rent_price)

apartment1=Apartment("zangvil",21,3000000,5000)

print(apartment1.tesuaa())



# #3

class Cat:
    def __init__(self,name,age,hair_color):
        self.__name=name
        self.__age=age
        self.__hair_color=hair_color

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age=age

    def getHairColor(self):
        return self.__hair_color

    def setHairColor(self,hair_color):
        self.__hair_color=hair_color

    def catVoice(self):
        return ("miao ")

    def mustash(self,there_is_mustash):
        if there_is_mustash=="yes":
            return "have mustash"
        else:
            return "no mustash"

    def __str__(self):
        return self.__name+" "+str(self.__age)+" "+self.__hair_color

cat1=Cat("mizi",7,"red")

print(cat1)
print(cat1.mustash(there_is_mustash="yes"))


4
class Car:
    def __init__(self,model,color,price):
        self.__model=model
        self.__color=color
        self.__price=price

    def getModel(self):
        return self.__model

    def setModel(self,model):
        self.__model=model

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color=color

    def getPrice(self):
        return  self.__price

    def setPrice(self,price):
        self.__price=price

    def __str__(self):
        return self.__model+" "+self.__color+" "+str(self.__price)

car1=Car("suzuki","orange",25000)
car2=Car("tesla","white",100000)
car3=Car("lamburgini","black",3500000)
car4=Car("mazda","gery",40000)

cars=[car1,
      car2,
      car3,
      car4]

def maxCars():
    max=0
    for i in range(len(cars)-1):
        if cars[i].getPrice()>cars[i+1].getPrice():
            max=cars[i]
        else:
            max=cars[i+1]

    return max

print(Car.__str__(maxCars()))

car1.wheels=4


#5
class Student:
    def __init__(self,name,id,birth_year,math_grade,history_grade,literature_grade,claSs):
        self.__name=name
        self.__id=id
        self.__math_grade=math_grade
        self.__history_grade=history_grade
        self.__literature_grade=literature_grade
        self.__claSs=claSs
        self.__birth_year=birth_year

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id=id

    def getMathGrade(self):
        return self.getMathGrade()

    def setMathGrade(self,math_grade):
        self.__math_grade=math_grade

    def getHistoryGrade(self):
        return self.__history_grade

    def setHistoryGrade(self,history_grade):
        self.__history_grade=history_grade

    def getLiteratureGrade(self):
        return self.__literature_grade

    def setLiteratureGrade(self,literature_grade):
        self.__literature_grade=literature_grade

    def getClaSs(self):
        return self.__claSs

    def setClaSs(self,claSs):
        self.__claSs=claSs

    def getBirthYear(self):
        return self.__birth_year

    def setBirthYear(self,birth_year):
        self.__birth_year=birth_year

    def age(self):
        return 2022-self.__birth_year

    def avg(self):
        return (self.__math_grade+self.__history_grade+self.__literature_grade)/3

    def diploma(self):
        return self.__name,self.__id,self.__claSs,self.__birth_year

    def gradediploma(self):
        print("Student name :",self.__name,"\nStudent id :",str(self.__id),"\nBirth year: ",str(self.__birth_year), "\nMath: ",str(self.__math_grade),"\nHistory:",str(self.__history_grade),"\nliterature",str(self.__literature_grade),"\nClass:",self.__claSs,"\nAverage grade: ",str(self.avg()))
        print()

        if  self.avg()>90:
            print("Excelent!")
        elif self.avg()<60:
            print("No Pass")

    def __str__(self):
        return "Student name :"+" "+self.__name+" "+"\nStudent id :"+" "+str(self.__id)+" "+"\nBirth year: "+" "+str(self.__birth_year)+" "+ "\nMath:" +" "+str(self.__math_grade) +" "+ "\nHistory:"+" "+str(self.__history_grade)+" "+"\nliterature: "+" "+str(self.__literature_grade)+" "+"\nClass:"+" "+self.__claSs


student1=Student("tsiona",312569000,1994,100,90,95,"QA")
student2=Student("dana",190929224,1993,50,50,60,"QA")
student3=Student("ofir",223344556,1995,70,80,90,"QA")
student4=Student("aviv",123456789,1996,90,100,97,"QA")


students=[student1,student2,student3,student4]

def topStudent(list):
    max=0
    for i in range(len(students)-1):
        if students[i].avg()> students[i+1].avg():
            max= students[i]
        else:
            max= students[i+1]

    return  max

print(topStudent(students))





