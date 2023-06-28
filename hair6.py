def f(n, m, songs):
    total_time = 0
    for i in range(m):
        total_time += songs[i]
        if total_time > n * 60:
            return i
    return "OK"
