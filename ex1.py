x1 = int(input('first x: '))
y1 = int(input('first y: '))
x2 = int(input('second x: '))
y2 = int(input('second y: '))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    dx_squared = dx**2
    dy_squared = dy**2

    sum_of_squares = dx_squared + dy_squared

    distance = sum_of_squares**0.5

    return distance

print(distance(x1, y1, x2, y2))