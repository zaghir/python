# operation numerique
value1 = 10 
value2 = 20 

# incrementation 
value1 += 1 
print(f" value1 {value1}")
type(value1)

# decrementation 
value1 -= 1 
print(f" value1 {value1}")
type(value1)

#divition 
print(f" value1 {value1/value2}")
type(value1/value2)

# recuperer la partie entiere d une division 
print(f" value1 {value1//value2}")
type(value1//value2)
value1 //= 2 
print(f" value1 {value1}")

# power ou puissance 
print(f"power 5**3 { 5**3}")

# convert flot to integer
print (f"convert flot to integer int(5.6) =  {int(5.6)}")

# convert integer to float
print (f"convert  integer to flot float(5) =  {float(5)}")

print(f" int(True) =  {int(True)} , int(False) = {int(False)} ")

# round 
print(f" rount(5.4) {round(5.4)}")
print(f" rount(5.5) {round(5.5)}")
print(f" rount(5.6) {round(5.6)}")
print(f" round(5.675 , 1) {round(5.675 , 1)}")
print(f" round(5.675 , 2) {round(5.675 , 2)}")
print(f" round(5.675 , 3) {round(5.675 , 3)}")

# all type is object in python 
is_even = True  # True != to true  true is not exist in python 
is_odd = False  #  
i = 10 
print(f" i > 15 {i > 15}")
print(f" i == 11 {i == 11}")
print(f" i == 10 {i == 10}")
print(f" i >= 5 {i >= 5}")

if (i > 10):
    print (f" if (i > 10)  yes")

i = 10 
j = 15 
if i%2 == 0 and j%2 == 0:
    print("i and j are even")
j = 14 
if i%2 == 0 and j%2 == 0:
    print("atleast one of i and j ")

if(True ^ False):
    print("condition True ^ False  this will print ")
x = 5 
if not x == 6 :
    print("x=5 , condition not x == 6   this will print")

if x != 6 :
    print("x=5 , condition not x != 6   this will print")

x = -6 
if x: 
    print(f" x = -6  != 0  condition if x   0 == False  this will print")

print(f" bool(-6) = {bool(-6)}  bool(0) = {bool(0)}")

i = 2 
if i == 1:
    print("i is 1")
elif i == 2:         
   print("i is 2")
elif i == 3 :
    print("i is 3")
else:
    print("i is not 1 or 2 or 3")

# premier fonction 
# avec python
def print_multiplication_table(table , start = 1 , end = 10) :
    for i in range(start , end + 1 ): 
        print(f"{table} * {i} = {table * i}")

print_multiplication_table(3) 

# Simple Interest 

def calculate_simple_intereset(principal , interest , duration) :
    return  principal * ( 1 + interest * 0.01 * duration )

print(calculate_simple_intereset(10000 , 5, 5))


# get value from input 

number1 = int(input("Enter number1 : "))
number2 = int(input("Enter number2 : "))

print("\n\n1 - Add")
print("2 - Substruct")
print("3 - Divide")
print("4 - Mulltiply")
print("5 - Exit")
 
choice = int(input("Choose your Operation :")) 

while choice != 5:
    if choice == 1 :
        result = number1 + number2
    elif choice == 2 :
        result = number1 - number2
    elif choice == 3 :
        result = number1 / number2
    elif choice == 4 :
        result = number1 * number2
    else: 
        result = "Invalide choice"
    print(result)
    choice = int(input("Choose your Operation :")) 

print("Thank You")





message = "hello world"
print("message {message.lower()}")

# import string module 
import string
char = "a"
vowel_string = "aeiouAEIOU"

print(f"---check a is a vowel {char in vowel_string}")

string_example = "This is a great thing"
for word in string_example : 
    print(f" --> {word}")

for word in string_example.split() : 
    print(f" split --> {word}")

print("repetition of str = test  * 10 ")
print("test "* 10)

# print in same lines 
i = 0 
print("print in same lines")
while(i < 5 ):
    print(i , end=" ")
    i +=1

for x in range(11 , 0 , -1):
    print(f" x =  {x}" , end=" ")

print("\n---> break with condition i == 5")
for i in range(1 , 11 ) :
    if i == 5 :
        break
    print(f" i =  {i}" , end=" ")

print("\n--->  continue")
for i in range(1 , 11):
    if i%2 == 0 :        
        continue
    print(i , end=" ")
print("Done")

import numbers
# index of loop 
numbers = [1 ,4, 7 , 9 , 0 ,6]
for number in numbers : 
    print(f"number = {number} " , end=" ")

for index , number in enumerate(numbers) :
    print(f" index = {index} - number = {number}")

print("--------------")
values = list("aeiou")
for index , vowel in enumerate(values) :
    print(f" index = {index} - vowel = {vowel}")

print("------if short cat--------")
isEven = number%2 == 0 
isEven = "Yes" if number %2 == 0 else "No"
print(f" number = {number} - isEven = {isEven}")

print(f"sum([10,20,30]  = {sum([10,20,30])}")

ma_variable ="test"
print(f"ma_variable ----> {ma_variable}")
del ma_variable
#print(f"ma_variable apres supression ----> {ma_variable}")


# class
class Country:
    pass

# pass permet de creer une class ou une methode vide 
india = Country()
usa = Country()
netherlands = Country()
india.name = "India"
india.capital = "new Delhi"
usa.name = "USA"
usa.capital = "Washington"
netherlands.name = "Netherlands"
netherlands.capital = "Amsterdam"
print(f" india {india.name}")

class MotorBike: 
    def __init__(self, speed):
        self.speed = speed
    
    def increase_speed( self  , how_much):
        self.speed += how_much
    def decrease_speed( self  , how_much):
        self.speed -= how_much
    

honda = MotorBike(50)

ducati = MotorBike(100)
print("------------")
print(f"honda.speed = {honda.speed}")
print(f"ducati.speed = {ducati.speed}")
# honda.speed = 250
# ducati.speed = 260
honda.increase_speed(50)
ducati.increase_speed(30)
print(f"honda.speed = {honda.speed}")
print(f"ducati.speed = {ducati.speed}")
honda.decrease_speed(50)
ducati.decrease_speed(30)

class Planet(object):
    def rotate(self):
        print("rotate")
    def revolve(self):
        print("revolve") 
    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()

earth = Planet()
earth.rotate_and_revolve()
        
marks = [10 , 20 ,30 ,40]

print(f"sum(marks) ===> {sum(marks)}")
print(f"average ===> {sum(marks) / len(marks) }")
print("marks.append(80) ")
marks.append(80)
print(f"average ===> {sum(marks) / len(marks) }")

print( f" max(marks) = {max(marks)}")
print( f" min(marks) = {min(marks)}")
print( f" len(marks) = {len(marks)}")
print(f" marks.insert(index , value)  (2,60)")
marks.insert(2 , 60)
marks.remove(60)
print(f" find 60 after remove it  ==> {60 in marks} ")

print(f"index of 20 in marks = {marks.index(20)} ")

for mark in marks:
    print(mark , end=" ")

print("-------- class student")
class Student :
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks
    def get_number_of_marks(self):
        return len(self.marks)
    def get_total_sum_of_marks(self):
        return sum(marks)
    def get_maximum_of_marks(self):
        return max(marks)
    def get_minimu_of_marks(self):
        return min(marks)
    def determine_average(self):
        return self.get_total_sum_of_marks()/self.get_number_of_marks()
    def add_new_mark(self , new_mark):
        self.marks.append(new_mark)
    def remove_mark_at_index(self , index):
        del self.marks[index]
    
student = Student("Mario" , [10 ,12 ,15,19] )
number = student.get_number_of_marks()
print(f"Student[number_of_marks-{student.get_number_of_marks()}]")
sum_of_marks= student.get_total_sum_of_marks()
maximum_mark = student.get_maximum_of_marks()
minimum_mark = student.get_minimu_of_marks()
average = student.determine_average()
student.add_new_mark(35)
student.remove_mark_at_index(3)
print(f"student.marks {student.marks}")
print(f"""
    Student[number_of_marks-{number} 
    sum_of_marks-{sum_of_marks} 
    max-{maximum_mark} min-{minimum_mark} 
    average-{average}""")

animals = ["Cat" , "Dog" , "Elephant" , "Fish"]
print(f"animals[2] ={animals[2]}")
# remove by value
animals.remove("Cat")
#remove by index 
del animals[2]
animals.append("Cat2")
animals.extend("Fish")
animals.extend(["Giraffe" , "Horse"])
animals = animals + ["Jackal" , "Kangaroo"]
animals += ["Lion" , "Monkey"]
animals.append(992124)
for animal in animals:
    print(animal , end=",")

# List Slicing
print("---- List Slicing")
numbers = ["Zero" , "One" , "Two","three" , "Four" , "Five" , "Six" , "Seven" , "Eigh" , "Nine"]
print(f" len(numbers) ==> {len(numbers)}")
print(f" numbers[2] ==>{numbers[2]}")
print(f" numbers[2:6] ==> {numbers[2:6]}")
print(f" numbers[:6] ==> {numbers[:6]}")
print(f" numbers[3:] ==> {numbers[3:]}")
print(f" numbers[1:8:3] ==> {numbers[1:8:3]}")
print(f" numbers[::3] ==> {numbers[::3]}")
print(f" numbers[::-1] ==> {numbers[::-1]}")
print(f" numbers[::-3] ==> {numbers[::-3]}")
print(f" del numbers[3:] ")
del numbers[3:]
print(f" del numbers[5:7] ")
del numbers[5:7]
print(f" numbers[3:7] = [3,4,5,6] ")
numbers[3:7] = [3,4,5,6]
print(f"numbers {numbers[0:]}")


print(f"numbers {numbers[0:]}")
numbers = ["Zero" , "One" , "Two","three" , "Four" , "Five" , "Six" , "Seven" , "Eigh" , "Nine"]
numbers.reverse()
print(f"numbers.reverse() ==> {numbers[0:]}")

numbers = ["Zero" , "One" , "Two","three" , "Four" , "Five" , "Six" , "Seven" , "Eigh" , "Nine"]
print(f"reversed(numbers) ")
for number in reversed(numbers) :
    print(number , end=",")
print("")    
print(f"numbers is not reverced {numbers[0:]}")

print("numbers.sort()")
numbers.sort()
print(f"numbers {numbers[0:]}")
numbers = ["Zero" , "One" , "Two","three" , "Four" , "Five" , "Six" , "Seven" , "Eigh" , "Nine"]
for number in sorted(numbers) :
    print(number , end=",")
print("")
print(f"numbers is not sorted {numbers[0:]}")

print("short by len")
for number in sorted(numbers , key=len) :
    print(number , end=",")

print("")
print("short by len and reverse")
for number in sorted(numbers , key=len , reverse=True) :
    print(number , end=",")
print("")

print("Use list as Stack ou Queue")
print("------Stack [FILO]")
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(f"{numbers[0:]}" )
print("numbers.pop()")
numbers.pop()
print(f"{numbers[0:]}" )
print("numbers.pop()")
numbers.pop()
print(f"{numbers[0:]}" )
print("numbers.append(55)")
numbers.append(55)
print(f"{numbers[0:]}" )

print("------Queue [FIFO]")
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(f"{numbers[0:]}" )
print("numbers.pop(0)")
numbers.pop(0)
print(f"{numbers[0:]}" )
print("numbers.pop(0)")
numbers.pop(0)
print(f"{numbers[0:]}" )

from operator import attrgetter
class Country2:
    def __init__(self , name , population , area):
        self.name = name
        self.population= population
        self.area = area

    def __repr__(self):
        return repr((self.name , self.population , self.area)) 

countries = [Country2("India" , 1500 , 100),
             Country2("China" , 2000 , 200),
             Country2("USA" , 120 , 300)]

countries.append(Country2("Russia" , 700 , 900))
print(countries)
print(countries[0:2])
print(f" sort by population {countries.sort(key=attrgetter('population') , reverse=True)}")
print(f" max  {max(countries , key=attrgetter('population'))}")
print(f" min  {min(countries , key=attrgetter('population'))}")

print("List comprehension ")
numbers = ["Zero" , "One" , "Two","three" , "Four" , "Five" , "Six" , "Seven" , "Eigh" , "Nine"]
print(numbers[0:])
numbers_length_four = [number for number in numbers]
print(f"numbers_length_four ==> {numbers_length_four} ")

numbers_length_four = [len(number) for number in numbers]
print(f" [len(number) for number in numbers]  ==> {numbers_length_four}")

numbers_length_four = [number.upper() for number in numbers]
print(f" [number.upper() for number in numbers]  ==> {numbers_length_four}")

numbers_length_four = [number for number in numbers if len(number) == 4 ]
print(f" [number for number in numbers if len(number) == 4]  ==> {numbers_length_four}")

values = [3,4,9,6,7,9,2,3,7]
values_even = []
values_even = [value for value in values if value % 2 ==0]
print(f"values_even ==> {values_even}")
values_odd = [value for value in values if value % 2 ==1]

print("Set----- doses not have duplicat values")
numbers = [1,2,3,2,1]
print(f" list of numbers ===> {numbers[0:]}")
numbers_set = set(numbers) 
print(f" set  of numbers ===> {numbers_set}")
numbers_set.add(8)
numbers_set.add(0)
numbers_set.remove(0)

# index is not supported in set numbers_set[0]

numbers_1_to_5_set = set(range(1,6))
numbers_4_to_10_set = set(range(4,11))


print(numbers_1_to_5_set)
print(numbers_4_to_10_set)
print("union of sets")
print(f"numbers_1_to_5_set | numbers_4_to_10_set ===> {numbers_1_to_5_set | numbers_4_to_10_set}")
print("intersection  of sets")
print(f"numbers_1_to_5_set & numbers_4_to_10_set ===> {numbers_1_to_5_set & numbers_4_to_10_set}")
print("substraction element of sets")
print(f"numbers_1_to_5_set - numbers_4_to_10_set ===> {numbers_1_to_5_set - numbers_4_to_10_set}")
print(f"numbers_4_to_10_set - numbers_1_to_5_set  ===> {numbers_4_to_10_set - numbers_1_to_5_set }")

print("Dictionary --- list [key:value] paire  like hash map in java")
occurances = dict(a=5 , b=6 , c=8)
print(f"occurances {occurances}")
print(f"occurances.get('a') ===> {occurances.get('a')} ") 
print("add ['d': '10'] ")
occurances['d'] = 10
print("return defaut value if not exist a key")
print(f"occurances.get('z' , -1 ) {occurances.get('z' , -1 )}")
print(f" get keys ===> {occurances.keys}")
print(f" get values ===> {occurances.values()}")
print(f" get items ===> {occurances.items()}")
for (key , value ) in occurances.items():
    print(f" [{key}:{value}]" , end="," )
print("del occurances['a']")
print(f" {occurances}")
del occurances['a']
print(f" {occurances}")

# key:value
# initial dictionnary
char_occurances = {} #[]
str = "This is an awesome occasion. This has never happened before."
for char in str : 

    char_occurances[char] = char_occurances.get(char , 0 ) + 1 
print("char_occurances")
print(char_occurances)

word_occurances = {} # []

for word in str.split() : 
    word_occurances[word] = word_occurances.get(word , 0 ) + 1
print(f"word_occurances")
print(word_occurances)

print("puzzels with Data structures")
str = "This is an awesome occasion. This has never happened before."
squares_first_ten_numbers = [ i*i for i in range(1 , 11)]
print(f"type(squares_first_ten_numbers)")
print(squares_first_ten_numbers) 
squares_first_ten_numbers_set = set(squares_first_ten_numbers)
squares_first_ten_numbers_set = {i*i for i in range(1 , 11)}
print(f"type(squares_first_ten_numbers_set)") 
print(squares_first_ten_numbers_set) 
squares_first_ten_numbers_dict = {i:i*i for i in range(1 , 11)}
print(f"type(squares_first_ten_numbers_dict)") 
print(squares_first_ten_numbers_dict) 

# print(f"type([]) ==> { type([]) }")
# print(f"type({}) ==> {type({})}")
# print(f"type(set()) ==> {type(set())}")
print("type([])")
print(type([]))
print("type({})")
print(type({}))
print("type(set())")
print(type(set()))
print("type({'A':5}")
print(type({'A':5}))
print("type(())")
print(type(()))
print("type((1,2,3,3))")
print(type((1,2,3,3)))


print("Tuples-------Is immutable much more efficient than a list")
def create_youssef() : 
    return "Youssef" , 1900 , 'Casablanca'

youssef = create_youssef()
print(type(youssef))
print("distructring")
name , year , country = youssef 
print(f" name-{name} year-{year} country-{country}")
print(f"len(youssef) ===>  { len(youssef)}")
print(f" youssef[0]-{youssef[0]} youssef[1]-{youssef[1]} youssef[2]-{youssef[2]}")
person = ("Youssef" , 5 , 'Casablanca')
print(f"person ===> {person}")
#swap value 
x = 0 
y = 1 
x , y = y ,x

x = (0)
print(type(x))
x = (0,)
x = 1,
print(type(x))


class Fan : 
    def __init__(self , make , radius , color):
        self.make= make 
        self.radius = radius 
        self.color = color
        self.speed = 0
        self.is_on = False
    
    def __repr__(self):
        return repr((self.make , self.radius , self.color , self.speed , self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3
    def switch_off(self):
        self.is_on = False
        self.speed = 0


fan = Fan('Manufacturer 1' , 5 ,'Red' )
print(fan)
fan.switch_on()
print(fan)

fan.switch_off()
print(fan)


class Book :
    def __init__(self , id , name , author ):
        self.id = id 
        self.name = name 
        self.author =author
        self.reviews = []
    
    def __repr__(self):
        return repr((self.id , self.name , self.author , self.reviews))
    
    def add_review(self , review):
        self.reviews.append(review)


class Review : 
    def __init__(self , id , description , rating):
        self.id = id 
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))    



book = Book( 100 , 'Book for Python', 'Youssef')

book.add_review(Review(10 , 'Great Book' ,5))
book.add_review(Review(12 , 'Awesome' ,5))
print(f"Book ===> {book}") 

#Heritage 
print("Heritage ------------ ")
class Animal:
    def bark(self):
        print("bark")


class Pet(Animal):
    def groom(self):
        print("groom")


animal = Animal()
animal.bark()

pet = Pet()
pet.groom()

#Heritage 
print("Heritage multiple ------------ ")

class LandAnimal: 
    def __init__(self) :
        super().__init__()
        self.walking_speed = 5 

    def increase_walking_speed(self , how_mach):
        self.walking_speed += how_mach


class WaterAnimal: 
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10
    
    def increase_swimming_speed(self , how_mach):
        self.swimming_speed += how_mach
    

class Amphibian(WaterAnimal , LandAnimal) : 
    def __init__(self):
        super().__init__()


amphibian = Amphibian()
print(amphibian.swimming_speed)
print(amphibian.walking_speed)
amphibian.increase_swimming_speed(10)
amphibian.increase_walking_speed(20)
print(amphibian.swimming_speed)
print(amphibian.walking_speed)


print("Abstract class ------ ")

from abc import ABC , abstractmethod
# herite de la ABC pour abstact class
class AbstractAnimal(ABC) :

    # definir la methode abstact avec l annotation  @abstratcmethod
    @abstractmethod
    def bark(self) :pass

# class Doc herite de la class AbstractAnimal
class Dog(AbstractAnimal):

    #redifinir la methode abstrat bark()
    def bark(self):
        print("Bow Bow")

Dog().bark()

print("template method pattern ------- ")
from abc import ABC , abstractmethod

class AbstractRecipe(ABC) :
    
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self) :pass

    @abstractmethod
    def recipe(self) :pass

    @abstractmethod
    def cleanup(self) :pass


class Recipe1 (AbstractRecipe) :

    def prepare(self) :
        print("do the dishes")
        print("get raw materials")

    def recipe(self) :
        print("execute the steps")

    def cleanup(self) :pass


class MicrowaveRecipe (AbstractRecipe) :

    def prepare(self) :
        print("do the dishes")
        print("get raw materials")
        print("switch on microwave")

    def recipe(self) :
        print("execute the steps")

    def cleanup(self) :
        print("switch off microwave")



Recipe1().execute()
MicrowaveRecipe().execute()

#Error handling

# helper 
print(" Press q to exit ---- ")
import builtins
# help(builtins)
print("help(builtins)")

print(" handling error with try:  except:  ---- ")
try:
    i = 2 
    j = 10 /i
    values = [1 , '1']
    sum(values)
except TypeError:
    print("exception --> TypeError")
    j = 10 
except ZeroDivisionError:
    print("exception --> ZeroDivisionError")
    j = 0 

print(f" j =  {j}")
print("End")

try:
    i = 0 
    j = 10 /i
except BaseException:
    print("exception --> BaseException")
    j = 0 
print("End")

try:
    i = 0 
    j = 10 /i
except Exception:
    print("exception --> Exception")
    j = 0
print("End")

try:
    sum([1 , '1'])
except (ZeroDivisionError , TypeError):
    print("exception --> Exception")
    j = 0 
print("End")

try:
    sum([1 , '1'])
except TypeError as error:
    print(error)
print("End")

# Open File/Resource

try:
    # Business Logic to read 
    i = 0
    j = 10 / i
    values = [1,2]
    sum(values)
except TypeError: 
    print("TypeError")
    j = 10
except ZeroDivisionError: 
    print("ZeroDivisionError")
    j = 0
else:
    print("Else")
finally:
    #Close file
    print("Finally")

print(j)
print("End")

#  USD 20
#  USD 20
#  USD 50
#  DH  500

class CurrenciesDoNotMatchError(Exception) :
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        

class Currency:
    def __init__(self , currency , amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency , self.amount))

    def __add__(self , other):
        if self.currency != other.currency:
            # raise Exception("Currency do not match")
            raise CurrenciesDoNotMatchError(self.currency + " "+ other.currency)
        total_amount = self.amount + other.amount
        return Currency(self.currency , total_amount)

value1 = Currency("USD" ,20)
value2 = Currency("USD" ,30)
value3 = Currency("DH" ,30)
print(f" value1(USD) + value2(USD)  {value1+ value2}" )
# print(f" value1(USD) + value3(DH)  {value1+ value3}" )


# Decimal number 
print("Decimal number ----------")
print(f" 4.5 - 3.2 = {4.5 - 3.2}"  )

print("with Decimal ----------")

# import decimal
from decimal import Decimal

value1 = Decimal('4.5')
value2 = Decimal('3.2')
print(f" 4.5 - 3.2 = {value1 - value2}")


import math

help(math.factorial)

# statistics --------
import statistics
print("Statictics ----- ")
marks = [1 , 6, 9, 23 ,2 ,7 ]
print(marks)
print(f" statistics.mean(mark) ===> {statistics.mean(marks)}")
print(f" statistics.median(mark) ===> {statistics.median(marks)}")
print(f" statistics.median_low(mark) ===> {statistics.median_low(marks)}")
print(f" statistics.variance(mark) ===> {statistics.variance(marks)}")


# Collection Module - deque for Queue and Stack 
print(" deque ---------")

from collections import deque
queue = deque(['Zero' , 'One' , 'Two'])
print(queue)
print("queue.pop()")
queue.pop()
print(" append -> Four , Five  appendleft -> Minus One")
queue.append('Four')
queue.append('Five')
queue.appendleft('Minus One')
print(queue)
print("queue.pop()")
queue.pop()
print(queue)
print("queue.popleft()")
queue.popleft()
print(queue)


#Date Module
print("Date ------ ")

import datetime
today_date = datetime.datetime.today()
print(f"datetime.datetime.today() ==>  {today_date}" )
print(f""" 
        today_date.year = {today_date.year}
        today_date.month = {today_date.month}
        today_date.day = {today_date.day}
        today_date.minute = {today_date.minute}
        today_date.second = {today_date.second}""")

some_date = datetime.datetime(2020 , 7 , 14 )
print(f"datetime.datetime(2020 , 7 , 14 ) ===> {some_date}")
some_date = datetime.datetime(2020 , 7 , 14  , 0 , 0)
print(f"datetime.datetime(2020 , 7 , 14  , 0 , 0) ===> {some_date}")
some_date = datetime.datetime(2020 , 7 , 14 , 21 , 5 , 38 , 224525)
print(f"datetime.datetime(2020 , 7 , 14 , 21 , 5 , 38 , 224525) ===> {some_date}")

# print(f"datetime.date() ==>  {datetime.date()}")
day = some_date 
print(f" day ")
print(f" ===> {day}")
print("day + datetime.timedelta(days = 90)")
print(f" ===> {day + datetime.timedelta(days = 90)}")
print("day + datetime.timedelta(weeks = 3)")
print(f" ===> {day + datetime.timedelta(weeks = 3)}")
print("day + datetime.timedelta(hours = 48)")
print(f" ===> {day + datetime.timedelta(hours = 48)}")


# Method  and  arguments 
def exemple_method(
    mandatory_parameter , 
    default_parameter ="Default" ,
    *args ,
    **keyword_args) :
    print(f"""
        mondatory_parameter = {mandatory_parameter} --- type ---> {type(mandatory_parameter)} 
        default_parameter = {default_parameter} --- type ---> {type(default_parameter)} 
        args = {args} --- type ---> {type(args)} 
        keyword_args = {keyword_args} --- type ---> {type(keyword_args)} 
    """)

print("exemple_method(15)")
exemple_method(15)
print("exemple_method(mandatory_parameter=15)")
exemple_method(mandatory_parameter=15)
print("exemple_method(15 , 'param1' , 'param2' , 'param3' , 'param4') param is all in args")
exemple_method(15 , 'param1' , 'param2' , 'param3' , 'param4')
print("exemple_method(15 , 'param1' , 'param2' , 'param3' , 'param4' , key1='a' , key2 ='b' , key3='c') ")
exemple_method(15 , 'param1' , 'param2' , 'param3' , 'param4' , key1='a' , key2 ='b' , key3='c' )
print("exemple_method( key1='a' , key2 ='b' , key3='c' , mandatory_parameter=15 , default_parameter = 'param4'  )")
exemple_method( key1='a' , key2 ='b' , key3='c' , mandatory_parameter=15 , default_parameter = 'param4'  )

example_list = [1,2,3,4,5,6]
print(example_list)
print("Unpacking args ----> exemple_method(*example_list)")
exemple_method(*example_list)

example_dict = {'a':'1' , 'b':'2' , 'c':'3'}
print(example_dict)
print("exemple_method(*example_list , **example_dict)")
exemple_method(*example_list , **example_dict)

print("Module --------- ")
print(" ")

import module_1
module_1.method_1()
module_1.ClassA().class_method_1()

import module_2
module_2.method_2()
module_2.ClassB().class_method_2()

print(" ")
# defining equality  for classes 
print('defining equality  for classes ')

class Student : pass 

student1 = Student()
student2 = Student()
print(f"id(student1) ==> {id(student1)}")
print(f"id(student2) ==> {id(student2)}")
print(f"student1 is student2 ==> {student1 is student2}")
print(f"comparing a reference of object ==> ")

student3 = student1 
print(f"id(student1) ==> {id(student1)}")
print(f"id(student3) ==> {id(student3)}")
print(f"student1 is student3 ==> {student1 is student3}")
print(f"student1 == student3 ==> {student1 == student3}")

class Student2 :
    def __init__(self , id):
        self.id = id
    def __repr__(self) :
        return repr(self.id)
    def __eq__(self , other) :
        return self.id == other.id

student1 = Student2(1)
student2 = Student2(2)
student3 = Student2(1)
student4 = student1
print(f"id(student1) ===> {id(student1)}  , {student1}")
print(f"id(student2) ===> {id(student2)}  , {student2}")
print(f"id(student3) ===> {id(student3)}  , {student3}")
print(f"id(student4) ===> {id(student4)}  , {student4}")

print(f"student1 is student4 == {student1 is student4})")
print(f"student1 is student2 == {student1 is student2})")
print(f"student1 is student3 == {student1 is student3})")
print(f"student1 == student3 == {student1 == student3})")


#None 
print(" ")
print("None --------")
print(f" type(None) {type(None)}")

def email(subject , content , to , cc = None  , bcc = None ) :
    print(f" subject = {subject} , content = {content} , to = {to} , cc = {cc}  , bcc = {bcc} ")

email("subject" , "greate work" , "to@gmail.com" )
email("subject" , "greate work" , "to@gmail.com" , None , None )
email(None , "greate work" , "to@gmail.com" , None , None )

var = None
if var is None : print(" do something")