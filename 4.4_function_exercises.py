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
    return s.lower() in "aeiou"


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
    return s.capitalize() if is_consonant(s[:1]) else s


assert capitalize_consonant("shoe") == "Shoe"
assert capitalize_consonant("baseball") == "Baseball"
assert capitalize_consonant("apple") == "apple"
assert capitalize_consonant("igloo") == "igloo"
assert capitalize_consonant("Baseball") == "Baseball"

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
    discount_amount = original_price * discount_percentage
    return original_price - discount_amount


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

# Recursive solution #1
# def remove_vowels(s, temp=""):
#     if not s:
#         return temp
#     return remove_vowels(s[1:], temp + s[:1] if not is_vowel(s[:1]) else temp)


# Recursive solution #2
# def remove_vowels(s, acc=""):
#     if s == "":
#         return acc

#     first, *rest = s
#     next = "".join(rest)

#     return remove_vowels(next, acc + first if first not in "aeiou" else acc)


def remove_vowels(s):
    return "".join([char for char in s if not is_vowel(char)])


assert remove_vowels("shoe") == "sh"
assert remove_vowels("test sentence") == "tst sntnc"
assert remove_vowels("bcdfghjk lmnpqrstvwxyz") == "bcdfghjk lmnpqrstvwxyz"
assert remove_vowels("ae io u") == "  "
assert remove_vowels("") == ""

# 10. Define a function named normalize_name. It should accept a string
# and return a valid python identifier.
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


def normalize_name(s):
    # anything that is not a valid python identifier should be removed
    for i in range(len(s)):
        if s[i].isalpha() or s[i] == "_":
            s = s[i:]
            break

    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores

    s = s.strip().lower().replace(" ", "_")
    return "".join([l for l in s if l.isalnum() or l in " _"])


assert normalize_name("Name") == "name"
assert normalize_name("First Name") == "first_name"
assert normalize_name("Completed") == "completed"
assert normalize_name("   First Name   ") == "first_name"
assert normalize_name("99 Completed") == "completed"
assert normalize_name("_Name  ") == "_name"
assert normalize_name("first_name") == "first_name"
assert normalize_name("% Completed") == "completed"
assert normalize_name(" email address@$") == "email_address"

# 11. Write a function named cumsum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# Recursive solution #1
# def cumsum(num_list, sum_list=[]):
#     if not num_list:
#         return sum_list

#     first_num = num_list[:1].pop()
#     last_sum = sum_list[-1] if sum_list else 0
#     return cumsum(num_list[1:], sum_list + [(first_num + last_sum)])

# Recursive solution #2
# def cumsum(l, acc=[]):
#     if len(l) == 0:
#         return acc
#     head, *tail = l
#     return cumsum(tail, acc + [head + acc[-1]] if acc else [head])


def cumsum(num_list):
    return [sum(num_list[: i + 1]) for i in range(len(num_list))]


assert cumsum([1, 1, 1]) == [1, 2, 3]
assert cumsum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert cumsum([]) == []
assert cumsum([0]) == [0]
assert cumsum([5]) == [5]

# Bonus
# 1. Create a function named twelveto24. It should accept a string in the
# format 10:45am or 4:30pm and return a string that is the representation of
# the time in a 24-hour format. Bonus write a function that does the opposite.


def twelveto24(time):
    hour, minute = time[:-2].split(":")
    period = time[-2:]
    if "am" == period:
        return f"0:{minute}" if hour == "12" else f"{hour}:{minute}"
    elif "pm" == period:
        if hour == "12":
            return f"{hour}:{minute}"
        else:
            return f"{int(hour) + 12}:{minute}"


assert twelveto24("10:45am") == "10:45"
assert twelveto24("4:30pm") == "16:30"
assert twelveto24("12:15pm") == "12:15"
assert twelveto24("12:34am") == "0:34"

# 2. Create a function named col_index. It should accept a spreadsheet column
# name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27


def col_index(column):
    pass


# 3. Write a function named `add`. It should accept two arguments and return
# the result of adding the two arguments together.


def add(n1, n2):
    return n1 + n2


assert add(1, 2) == 3
assert add(100, 50) == 150
assert add(-1, 5) == 4
assert add(-5, -10) == -15

# 4. Write a function named `subtract`. It should accept two arugments and
# return the result of subtracting the first from the second.


def subtract(n1, n2):
    return add(n1, -n2)


assert subtract(4, 1) == 3
assert subtract(-5, 3) == -8
assert subtract(-6, -10) == 4

# 5. Write a function named `multiply`. It should accept two numbers and
# return the result of multiplying them together.


# def multiply(n1, n2):
#     if n2 == 1:
#         return n1
#     else:
# FIXME: this doubles n1 every time
#         return multiply(add(n1, n1), n2 - 1)


# assert multiply(2, 2) == 4
# assert multiply(10, 5) == 50
# assert multiply(4, -5) == -20
# assert multiply(-4, -10) == 40

# Bonus: don't use the `*` operator in your `multiply` function
# Bonus Bonus: don't use a loop in your `multiply` function
