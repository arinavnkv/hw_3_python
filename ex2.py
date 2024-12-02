a = float(input('a = '))
n = int(input('n = '))

def power(a, n):
    result = 1

    if n < 0:
        a = 1 / a
        n = -n

    for _ in range(n):
        result *= a

    return result

print(power(a, n))