import pprint

# 1. Import and test 3 of the functions from your functions exercise file.

# Your functions exercise are not currently in a file with a name that
# can be easily imported. Copy your functions exercise file and name the
# copy functions_exercises.py.

# Import each function in a different way:

# import the module and refer to the function with the . syntax
import function_exercises

assert function_exercises.capitalize_consonant("q") == "Q"
assert function_exercises.cumsum([1, 2, 3]) == [1, 3, 6]
assert function_exercises.normalize_name(" email address@$") == "email_address"

# use from to import the function directly
from function_exercises import capitalize_consonant
from function_exercises import cumsum
from function_exercises import normalize_name

assert capitalize_consonant("q") == "Q"
assert cumsum([1, 2, 3]) == [1, 3, 6]
assert normalize_name(" email address@$") == "email_address"

# use from and give the function a different name
from function_exercises import capitalize_consonant as capcon
from function_exercises import cumsum as cs
from function_exercises import normalize_name as normname

assert capcon("q") == "Q"
assert cs([1, 2, 3]) == [1, 3, 6]
assert normname(" email address@$") == "email_address"

###############################################################################

# For the following exercises, read about and use the itertools module
# from the standard library to help you solve the problem.
from itertools import filterfalse, combinations, permutations, product

# How many different ways can you combine the letters from "abc"
# with the numbers 1, 2, and 3? E.g., [(a, 1), (a, 2), (a, 3), (b, 1), etc.]

solution1 = [
    ("a", 1),
    ("a", 2),
    ("a", 3),
    ("b", 1),
    ("b", 2),
    ("b", 3),
    ("c", 1),
    ("c", 2),
    ("c", 3),
]

# first way
print("1st:")
output1 = list(filterfalse(lambda t: t[0] == t[1], product("abc", (1, 2, 3))))
pprint.pprint(output1, width=31, compact=True)
assert output1 == solution1
print()

# second way
print("2nd:")
output2 = list(
    filterfalse(
        lambda t: isinstance(t[0], int) or isinstance(t[1], str),
        combinations(("a", "b", "c", 1, 2, 3), 2),
    )
)
assert output2 == solution1
pprint.pprint(output2, width=31, compact=True)
print()

# third way
print("3rd:")
output3 = [p for p in product("abc", (1, 2, 3))]
pprint.pprint(output3, width=31, compact=True)
output3 == solution1
print()

# How many different ways can you combine two of the letters from "abcd"?
# E.g., [(a, b), (a, c), (a, d), (b, a), etc]

solution2 = [
    ("a", "b"),
    ("a", "c"),
    ("a", "d"),
    ("b", "a"),
    ("b", "c"),
    ("b", "d"),
    ("c", "a"),
    ("c", "b"),
    ("c", "d"),
    ("d", "a"),
    ("d", "b"),
    ("d", "c"),
]

# first way
print("1st:")
output1 = list(permutations("abcd", 2))
pprint.pprint(output1, width=38, compact=True)
assert output1 == solution2
print()

# second way
print("2nd:")
output2 = list(filterfalse(lambda t: t[0] == t[1], product("abcd", "abcd")))
pprint.pprint(output2, width=38, compact=True)
assert output2 == solution2
print()

# third way
print("3rd:")
output3 = [p for p in product("abcd", "abcd") if p[0] != p[1]]
pprint.pprint(output3, width=38, compact=True)
assert output3 == solution2
print()

###############################################################################

# Save this file as profiles.json inside of your exercises directory.
# Use the load function from the json module to open this file,
# it will produce a list of dictionaries. Using this data, write some
# code that calculates and outputs the following information:
from json import load

with open("profiles.json") as f:
    profiles = load(f)


# Total number of users
nusers = len(profiles)
print("Total users:", nusers)
assert nusers == 19

# Number of active users
nactive = sum(d["isActive"] for d in profiles)
print("Total active users:", nactive)
assert nactive == 9

# Number of inactive users
ninactive = sum(not d["isActive"] for d in profiles)
print("Number of inactive users:", ninactive)
assert ninactive == 10

# Grand total of balances for all users


def currency_to_float(currency):
    return float(currency.replace("$", "").replace(",", ""))


balances = [currency_to_float(d["balance"]) for d in profiles]
total_balances = sum(balances)
print("Grand total of balances for all users:", total_balances)
assert total_balances == 52667.02

# Average balance per user
avgbalance = round(total_balances / nusers, 2)
print("Average balance per user:", avgbalance)
assert avgbalance == 2771.95

# User with the lowest balance


def user_with_balance(users, balance):
    """
    users is a list of dictionaries containing user data
    balance is a string in the format $100.00
    """
    return [d["name"] for d in profiles if d["balance"] == balance][0]


def float_to_currency(amount):
    return f"${amount:,.2f}"


usr_min_bal = user_with_balance(profiles, float_to_currency(min(balances)))
print("User with the lowest balance:", usr_min_bal)
assert usr_min_bal == "Avery Flynn"

# User with the highest balance
usr_max_bal = user_with_balance(profiles, float_to_currency(max(balances)))
print("User with the highest balance", usr_max_bal)
assert usr_max_bal == "Fay Hammond"

# Most common favorite fruit
most_fav_fruit = max([d["favoriteFruit"] for d in profiles])
print("Most common favorite fruit:", most_fav_fruit)
assert most_fav_fruit == "strawberry"

# Least most common favorite fruit
least_fav_fruit = min([d["favoriteFruit"] for d in profiles])
print("Least most common favorite fruit:", least_fav_fruit)
assert least_fav_fruit == "apple"

# Total number of unread messages for all users
nunread = sum([int(sorted(d["greeting"].split())[0]) for d in profiles])
print("Total number of unread messages for all users:", nunread)
assert nunread == 210
