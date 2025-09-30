def score(x, y):
    distance_squared = x**2 + y**2
    if distance_squared > 100:
        return 0
    elif distance_squared > 25:
        return 1
    elif distance_squared > 1:
        return 5
    else:
        return 10
