def f():
    answers = [input().split() for _ in range(5)]
    correct_count = sum(1 for d, e in answers if d == e)
    return "OK" if correct_count >= 3 else "NG"


result = f()
print(result, end="")
