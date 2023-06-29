def f(p):
    return p // 100 + 10 if p >= 1000 else p // 100


def a(p):
    points = f(p)
    return points


p = int(input())
result = a(p)
print(result)
