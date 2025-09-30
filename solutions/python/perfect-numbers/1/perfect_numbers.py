def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum([i for i in range(1, number) if number % i == 0])
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"


# sum([i for i in range(1, number) if number % i == 0])

# range(1, number)
# - Generates numbers from 1 up to (but not including) number
# - Example: if number = 6, this gives [1, 2, 3, 4, 5]

# for i in range(1, number)
# - Loops through each number in that range
# - i takes values 1, 2, 3, 4, 5 (for number = 6)

# if number % i == 0
# - % is the modulo operator (gives remainder after division)
# - number % i == 0 checks if i divides evenly into number (no remainder)
# - This finds all **divisors** of the number
# - Example: for number = 6:
#   - 6 % 1 = 0 ✓ (1 divides 6)
#   - 6 % 2 = 0 ✓ (2 divides 6)
#   - 6 % 3 = 0 ✓ (3 divides 6)
#   - 6 % 4 = 2 ✗ (4 doesn't divide 6)
#   - 6 % 5 = 1 ✗ (5 doesn't divide 6)

# [i for ... ]
# - Creates a list of all i values that pass the condition
# - For number = 6: [1, 2, 3]

# sum(...)**
# - Adds all numbers in the list
# - For number = 6: sum([1, 2, 3]) = 6
