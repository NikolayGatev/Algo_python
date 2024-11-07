def calc_fib_iter(number): # iterative solutions
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib1 + fib0
        fib0, fib1 = fib1, result
    return result

print(calc_fib_iter(50))

def calc_fib_recurs(number): # recursive solution
    if number <= 1:
        return 1
    return  calc_fib_recurs(number - 1) + calc_fib_recurs(number - 2)