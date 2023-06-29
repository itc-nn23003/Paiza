def f():
    c1, p1 = map(int, input().split())
    c2, p2 = map(int, input().split())
    A = c1 / p1
    B = c2 / p2
    return 1 if A > B else 2


output = f()
print(output)
