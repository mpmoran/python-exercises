# 1. Define a function named is_two. It should accept one input and return
# True if the passed input is either the number or the string 2,
# False otherwise.


def is_two(num):
    return num == 2 or num == "2"


assert is_two(2)
assert is_two("2")
assert not is_two(5)
assert not is_two("a")

# 2. Define a function named is_vowel. It should return True if the
# passed string is a vowel, False otherwise.


def is_vowel(s):
    vowels = ["a", "e", "i", "o", "u"]
    return len(s) == 1 and s.lower() in vowels


assert is_vowel("a")
assert is_vowel("O")
assert is_vowel("u")
assert not is_vowel("apple")
assert not is_vowel("Z")
assert not is_vowel("t")

# 3. Define a function named is_consonant. It should return True if the
# passed string is a consonant, False otherwise. Use your is_vowel
# function to accomplish this.


def is_consonant(s):
    return not is_vowel(s)


assert is_consonant("z")
assert is_consonant("b")
assert is_consonant("L")
assert not is_consonant("a")
assert not is_consonant("U")

# 4. Define a function that accepts a string that is a word. The function
# should capitalize the first letter of the word if the word starts with
# a consonant.


def capitalize_consonant(s):
    first = s[0]
    rest = s[1:]
    return first.upper() + rest if is_consonant(first) else s


assert capitalize_consonant("shoe") == "Shoe"
assert capitalize_consonant("baseball") == "Baseball"
assert capitalize_consonant("apple") == "apple"
assert capitalize_consonant("igloo") == "igloo"

# 5. Define a function named calculate_tip. It should accept a
# tip percentage (a number between 0 and 1) and the bill total, and
# return the amount to tip.


def calculate_tip(tip_percentage, bill_total):
    return round(tip_percentage * bill_total, 2)


assert calculate_tip(0.2, 100) == 20
assert calculate_tip(0.5, 50) == 25
assert calculate_tip(0, 500) == 0
assert calculate_tip(1, 20) == 20

# 6. Define a function named apply_discount. It should accept a
# original price, and a discount percentage, and return the
# price after the discount is applied.


def apply_discount(original_price, discount_percentage):
    return round(original_price * (1 - discount_percentage), 2)


assert apply_discount(100, 0.5) == 50
assert apply_discount(50, 0.8) == 10
assert apply_discount(20, 0) == 20
assert apply_discount(25, 1) == 0

# 7. Define a function named handle_commas. It should accept a string
# that is a number that contains commas in it as input, and
# return a number as output.


def handle_commas(s):
    return int(s.replace(",", ""))


assert handle_commas("1,000") == 1000
assert handle_commas("50,000,000") == 50_000_000
assert handle_commas("4") == 4
assert handle_commas("98765") == 98765

# 8. Define a function named get_letter_grade. It should accept a
# number and return the letter grade associated with that number (A-F).


def get_letter_grade(grade):
    grade_map = {
        "A": range(90, 101),
        "B": range(80, 90),
        "C": range(70, 80),
        "D": range(60, 70),
        "F": range(0, 60),
    }

    for letter in grade_map.keys():
        if grade in grade_map[letter]:
            return letter


assert get_letter_grade(100) == "A"
assert get_letter_grade(95) == "A"
assert get_letter_grade(90) == "A"
assert get_letter_grade(89) == "B"
assert get_letter_grade(84) == "B"
assert get_letter_grade(80) == "B"
assert get_letter_grade(79) == "C"
assert get_letter_grade(74) == "C"
assert get_letter_grade(70) == "C"
assert get_letter_grade(69) == "D"
assert get_letter_grade(66) == "D"
assert get_letter_grade(60) == "D"
assert get_letter_grade(59) == "F"
assert get_letter_grade(50) == "F"
assert get_letter_grade(0) == "F"


# 9. Define a function named remove_vowels that accepts a string and
# returns a string with all the vowels removed.


def remove_vowels(s):
    for letter in s:
        if is_vowel(letter):
            return remove_vowels(s.replace(letter, ""))

    return s


assert remove_vowels("shoe") == "sh"
assert remove_vowels("test sentence") == "tst sntnc"
assert remove_vowels("bcdfghjk lmnpqrstvwxyz") == "bcdfghjk lmnpqrstvwxyz"
assert remove_vowels("ae io u") == "  "

# 10. Define a function named normalize_name. It should accept a string
# and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# 11. Write a function named cumsum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# Bonus
# 1. Create a function named twelveto24. It should accept a string in the
# format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# 2. Create a function named col_index. It should accept a spreadsheet column
# name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
