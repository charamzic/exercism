def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if not digits:
        return [0]

    decimal_number = 0
    for digit in digits:
        decimal_number = decimal_number * input_base + digit

    if decimal_number == 0:
        return [0]

    result = []
    while decimal_number > 0:
        remainder = decimal_number % output_base
        result.append(remainder)
        decimal_number = decimal_number // output_base

    result.reverse()
    return result
