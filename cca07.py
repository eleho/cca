order = '1,2013-07-25 00:00:00.0,11598,CLOSED'
orderStatus = order.split(",")
 #order.isprintable() # use in commandline

def printMax(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        print(str(x) + " is maximum")
    else:
        print(str(y) + " is maximum")

printMax(2, 3)

def printMax2(x, y):
    '''Prints the maximum of two numbers...
    both the numbers should be integers'''
    if x > y:
        print(str(x) + " is maximum")
    else:
        print(str(y) + " is maximum")

printMax2(5, 3)
#printMax2.__doc__()
print(printMax2(20,32))

def min_max(numbers):
    smallest=largest=numbers[0]
    for item in numbers:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest

print(min_max([1, 2, 5, 3, 7, 8, 4]))

smallest,largest=min_max([1, 2, 5, 3, 7, 8, 4])
print(smallest)
print(largest)
