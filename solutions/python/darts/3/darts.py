def score(x, y):
    distance_squared = x**2 + y**2

    circles = [
        (1, 10),
        (25, 5),
        (100, 1),
    ]

    for radius_squared, points in circles:
        if distance_squared <= radius_squared:
            return points

    return 0
