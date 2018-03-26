import random
import sys
import os

#Basic

print("Hello Krishna")
name = "Krish"
print(name)
quote = "\"Always remember you are unique"
multiline_quote = ''' just
like everyone else'''
print("%s %s %s" % ('I like the quote', quote, multiline_quote))
print('\n' * 5)
print("I dont like ", end="")
print("newlines")

#Lists

grocery_list = ['Bananas','Apples','Kale'
                ,'Tomatoes']
print('First Item', grocery_list[0])
grocery_list[0] = "Green Bananas"
print('First Item', grocery_list[0])
print(grocery_list[1:3])
other_events = ['Wash Car','Make Dinner']
to_do_list = [grocery_list, other_events]
print(to_do_list)
print(to_do_list[0][0])
grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1, "Pickle")
print(to_do_list)
grocery_list.remove("Pickle")
print(to_do_list)
grocery_list.sort()
grocery_list.reverse()
print(to_do_list)

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#Tuples = unlike list, we cannot change tuple after it is created. Sometime data which should not be changed.

pi_tuple = (1,2,3,4,5,6,7,8,4,2)
print(pi_tuple)

new_tuple = list(pi_tuple)
print(new_tuple[4])
new_list = tuple(new_tuple)

print(len(new_tuple))
print(max(new_tuple))
print(min(new_tuple))
new_tuple.sort()

#dictionary = cannot be + liked list

super_villians = {'Krish' : 'Krishna',
                  'Shree' : 'Shriram',
                  'Adi' : 'Adesh'}

print(super_villians['Shree'])

del super_villians['Adi']

super_villians['Shree'] = 'Shriram Nandkishore'

print(len(super_villians))
print(super_villians.get("Shree"))
print(super_villians.keys())
print(super_villians.values())

#Conditional if else elif
age = 26

if age > 16:
    print('You are fucking old enough to vote')
else :
    print('You are a loser')

if age < 16:
    print('You are fucking old enough to vote')
elif age == 21:
    print('You are a blackjack')
else :
    print('You are a loser')

#Logical operators and or not
if ((age >= 1) and (age <=18)):
    print('You may fyck')
elif ((age == 21) or (age >= 65)):
    print('You may stilll fuck')
elif not(age == 21):
    print('You already fuck')
else:
    print('loser')

#Looping for

for y in grocery_list:
    print(y)

to_do_list.append(['Krish','Shri'])

for x in range(0,3):
    for y in range(0,2):
        print(to_do_list[x][y])

#while

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i +=1

#functions

def addNumber(a,b):
    print('',a+b)
addNumber(1,2)

print('What is your name')
#your = sys.stdin.readline()
#print('Hello', your)

#String functions
long_string = "i'll love you till the last breath"

print(long_string[0:4])
print(long_string[-6:])
print(long_string[5:-4])
print(long_string[:4] + "Mansi")

print("%c is my %s letter and my number %d number is %.5f" %('x', 'sex', 1 , .14))

print(long_string.capitalize())

print(long_string.find("love"))

print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("love", "sex"))
print(long_string.strip())

#convert string to list
quote_list = long_string.split(" ")
print(quote_list)

#FILE I/O

test_file = open("test.txt", "wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()
test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

#to delete the file
#os.remove("test.txt")

#OBjects : Class, objects, inheritance,

#__ variables are private

class Animal:
    __naav = None
    __height = None
    __weight = None
    __sound = None


#constructor
    def __init__(self, naav, height, weight, sound):
        self.__naav = naav
        self.__height = height
        self.__weight = weight
        self.__sound = sound

#encapsulation

    def set_naav(self, naav):
        self.__naav = naav

    def get_naav(self):
        return self.__naav

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

#polymorphism

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilos and says {}".format(self.__naav,
                                                                 self.__height,
                                                                 self.__weight,
                                                                 self.__sound)

cat = Animal('Budsy', 33, 10, 'Meow')

print(cat.toString())


#Inheritance

class Dog(Animal):
    __owner = None

    def __init__(self, naav, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(naav, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilos and says {} his owner is {}".format(self.get_naav(),
                                                                                  self.get_height(),
                                                                                  self.get_weight(),
                                                                                  self.get_sound(),
                                                                                  self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog('Spot', 53, 27, 'Bhujo', 'Krish')

print(spot.toString())







