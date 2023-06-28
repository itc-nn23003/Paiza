def f(s, t):
    A = "".join(["+" if i == t else "-" for i in range(1, s + 1)])
    return A


s = int(input())
t = int(input())

result = f(s, t)
print(result)
