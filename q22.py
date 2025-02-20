#Write a program that will tell the number of 
# dogs and chicken are there when the user 
# will provide the value of total heads and legs.


def count_animals(heads, legs):
    for chickens in range(heads + 1):  # Chickens can range from 0 to total heads
        dogs = heads - chickens  # Remaining are dogs
        if (2 * chickens + 4 * dogs) == legs:  # Check if legs match
            return chickens, dogs
    return "No valid solution found"

# Input from user
total_heads = int(input("Enter total number of heads: "))
total_legs = int(input("Enter total number of legs: "))

result = count_animals(total_heads, total_legs)
if isinstance(result, tuple):
    print(f"Number of Chickens: {result[0]}")
    print(f"Number of Dogs: {result[1]}")
else:
    print(result)
