def fact_get(n):
    if n <= 1:
        return 1
    return n * (fact_get(n - 1))


n = int(input())
print(fact_get(n))
