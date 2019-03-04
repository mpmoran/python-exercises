# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is
# Monday or not
day_of_week = input("Enter a day of the week: ")
if day_of_week == "Monday":
    print("You entered " + day_of_week + ".")
else:
    print("You did not enter Monday.")

print()

# b. prompt the user for a day of the week, print out whether the day is a
# weekday or a weekend
day_of_week = input("Enter a day of the week: ")
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
if day_of_week.title() in weekday:
    print(day_of_week + " is a weekday.")
elif day_of_week.title() in weekend:
    print(day_of_week + " is a weekend.")
else:
    print(day_of_week + " is not a day of the week.")

print()

# c. create variables and make up values for
#   the number of hours worked in one week
weekly_hours_worked = 43
#   the hourly rate
hourly_rate = 15
overtime_rate = hourly_rate * 1.5
#   how much the week's paycheck will be

# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours
if weekly_hours_worked >= 0 and weekly_hours_worked <= 40:
    weekly_paycheck = weekly_hours_worked * hourly_rate
    print(weekly_paycheck)
elif weekly_hours_worked > 40:
    weekly_paycheck = (
        hourly_rate * 40 + (weekly_hours_worked - 40) * overtime_rate
    )
    print(weekly_paycheck)
else:
    print("Wrong number of hours worked")

print()

# 2. Loop Basics

# a. While

# Create an integer variable i with a value of 5.
i = 5

# Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    # Each loop iteration, output the current value of i, then increment i
    # by one.
    print(i)
    i += 1
print()

# Your output should look like this:

# 5 6 7 8 9 10 11 12 13 14 15

# Create a while loop that will count by 2's starting with 0 and ending at
# 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

print()

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

print()

# Create a while loop that starts at 2, and displays the number squared
# on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1_000_000:
    print(i)
    i **= 2

print()

# 2 4 16 256 65536

# Write a loop that uses print to create the output shown below.
i = 100

while i > 0:
    print(i)
    i -= 5

print()

# b. For Loops

# i. Write some code that prompts the user for a number, then shows a
# multiplication table up through 10 for that number.
user_num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{user_num} x {i} = {user_num * i}")

print()

# ii. Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(str(i) * i)

print()

# c. break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break
# statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers
# between 1 and 50, except for the number the user entered.
user_num = input("Enter an odd number between 1 and 50: ")
while not user_num.isdigit() or int(user_num) % 2 == 0:
    user_num = input("Enter an odd number between 1 and 50: ")
print()
print("Number to skip is:", int(user_num))
print()
for i in range(1, 51, 2):
    if i == int(user_num):
        print("Yikes! Skipping number:", i)
        continue
    print("Here is an odd number:", i)

print()

# d. The input function can be used to prompt for input and use that input in
# your python code. Prompt the user to enter a positive number and write a
# loop that counts from 0 to that number. (Hints: first make sure that the
# value the user entered is a valid number, also note that the input function
# returns a string, so you'll need to convert this to a numeric type.)
user_num = input("Enter a positive number: ")
while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Enter a positive number: ")

for i in range(int(user_num) + 1):
    print(i)

print()

# e. Write a program that prompts the user for a positive integer. Next write
# a loop that prints out the numbers from the number the user entered down
# to 1.
user_num = input("Enter a positive number: ")
while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Enter a positive number: ")

for i in range(int(user_num), 0, -1):
    print(i)

print()

# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is
# the FizzBuzz test. Developed by Imran Ghory, the test is designed to test
# basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
for i in range(1, 101):
    # For numbers which are multiples of both three and five print "FizzBuzz"
    if i % 5 == 0 and i % 3 == 0:
        print(i, "FizzBuzz")
    # For multiples of three print "Fizz" instead of the number
    elif i % 3 == 0:
        print(i, "Fizz")
    # For the multiples of five print "Buzz".
    elif i % 5 == 0:
        print(i, "Buzz")

print()

# 4. Display a table of powers.

wants_to_continue = "y"
while wants_to_continue.lower() == "y" or wants_to_continue.lower() == "yes":
    # Prompt the user to enter an integer.
    user_num = input("What number would you like to go up to? ")

    print("\nHere is your table!\n")
    print("number | squared | cubed")
    print("------ | ------- | -----")
    # Display a table of squares and cubes from 1 to the value entered.
    for i in range(1, int(user_num) + 1):
        print(f"{i: 6} | {i ** 2: 7} | {i ** 3: 5}")

    # Ask if the user wants to continue.
    wants_to_continue = input("\nWould you like to continue? ")
    # Assume that the user will enter valid data.
    # Only continue if the user agrees to.

print()

# Bonus: Research python's format string specifiers to align the table

# 5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
wants_to_continue = "y"
while wants_to_continue.lower() == "y" or wants_to_continue.lower() == "yes":
    grade = int(input("Enter a numerical grade from 0 to 100: "))

    # Display the corresponding letter grade.
    if grade >= 0 and grade <= 59:
        print(f"{grade} is an F.")
    elif grade <= 66:
        print(f"{grade} is a D.")
    elif grade <= 79:
        print(f"{grade} is a C.")
    elif grade <= 87:
        print(f"{grade} is a B.")
    elif grade <= 100:
        print(f"{grade} is an A.")

    # Prompt the user to continue.
    # Assume that the user will enter valid integers for the grades.
    # The application should only continue if the user agrees to.
    wants_to_continue = input("\nWould you like to continue? ")

print()
# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# 6. Create a list of dictionaries where each dictionary represents a book
# that you have read. Each dictionary in the list should have the keys title,
# author, and genre. Loop through the list and print out information about
# each book.
books_read = [
    {"title": "Fire and Fury", "author": "Michael Wolff", "genre": "History"},
    {"title": "Fear", "author": "Bob Woodward", "genre": "History"},
    {"title": "Reporter", "author": "Seymour Hersh", "genre": "Memoir"},
    {"title": "Gilded Age", "author": "Mark Twain", "genre": "Fiction"},
    {
        "title": "Battle Cry of Freedom",
        "author": "James McPherson",
        "genre": "History",
    },
    {
        "title": "Uncle Tom's Cabin",
        "author": "Harriet Beecher Stowe",
        "genre": "Fiction",
    },
]

for book in books_read:
    print(f"{book['title']} by {book['author']} in genre {book['genre']}")

# a. Prompt the user to enter a genre, then loop through your books list and
# print out the titles of all the books in that genre.
user_genre = input("\nEnter a book genre: ")
print(f"Books I have read in genre {user_genre}:")
for book in books_read:
    if book["genre"] == user_genre.title():
        print(f"{book['title']}")
