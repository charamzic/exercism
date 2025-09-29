def square_root(number):
    if number == 0:
        return 0

    left, right = 1, number
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            left = mid + 1
        else:
            right = mid - 1

    return right
