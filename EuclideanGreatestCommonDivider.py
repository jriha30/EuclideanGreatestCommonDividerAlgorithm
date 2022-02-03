import timeit

@profile
def WhileGCD(m, n):
    while m != 0:
        l = m
        m = n % m
        n = l
    return n

@profile
def RecursionGCD(m, n):
    if m == 0:
        return n
    return RecursionGCD(n % m, m)

def TestLoop():
    WhileGCD(123454321,7654345432343)

def TestRecursion():
    RecursionGCD(123454321,7654345432343)

TestLoop()
TestRecursion()

# print(timeit.Timer(TestLoop).timeit(number=100000))
# print(timeit.Timer(TestRecursion).timeit(number=100000))