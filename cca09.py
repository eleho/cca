def sumOfInteger(lb, ub):
    l = lb - 1
    return((ub * (ub + 1)) / 2) - ((l * (l + 1)) / 2)

print(sumOfInteger(1, 10))
print(sumOfInteger(5, 10))

def sum(lb, ub):
    total = 0
    for i in range(lb, ub + 1):
        total += i
    return total

print(sum(1, 10))
print(sum(5, 10))

def sum(lb, ub, f):
    total = 0
    for i in range(lb, ub + 1):
        print(f(i))
        total += f(i)
    return total

print(sum(5, 10, lambda i: i))
print(sum(5, 10, lambda i: i * 2))
print(sum(5, 10, lambda i: i if(i%2 == 0) else 0))

def getEven(n):
    return n if(n%2 == 0) else 0

print(sum(5, 10, lambda i: getEven(i)))
