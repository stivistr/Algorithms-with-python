def func_fact(n):
    if n == 0:
        return 1
    return n * func_fact(n - 1)


n = int(input())

print(func_fact(n))