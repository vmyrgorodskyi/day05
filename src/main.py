#lesson48
'''
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
'''

#lesson 49
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height = total_height + height

number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + 1

avg_height = round(total_height / number_of_students)
print(avg_height)
'''

#lesson50
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
#        print(highest_score)

print(highest_score)
'''

#lesson 51

#for number in range(1, 11, 3):
#    print(number)

#total = 0
#for number in range(1, 101):
#    total += number
#print(total)

'''
#lesson52
total_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_even += number
print(total_even)
'''

#lesson53
'''
total = 0

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
'''

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

nr_letters_iterator = 1
nr_numbers_iterator = 1
nr_symbols_iterator = 1
password_list = []


for letter in letters:
    if nr_letters_iterator <= nr_letters:
        nr_letters_iterator = nr_letters_iterator + 1
        password_list.append(random.choice(letters))


for number in numbers:
    if nr_numbers_iterator <= nr_numbers:
        nr_numbers_iterator = nr_numbers_iterator + 1
        password_list.append(random.choice(numbers))

for symbol in symbols:
    if nr_symbols_iterator <= nr_symbols:
        nr_symbols_iterator = nr_symbols_iterator + 1
        password_list.append(random.choice(symbols))

#password = password.split(',')
random.shuffle(password_list)
#print(password)

password = ""

for char in password_list:
    password = password + char

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P