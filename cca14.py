def readData(dataPath):
    dataFile = open(dataPath)
    dataStr = dataFile.read()
    dataList = dataStr.splitlines()
    return dataList

orders = readData('/data/retail_db/orders/part-00000')

# orders[:10]
for i in orders[:10]:
    print(i)
    print(i.split(',')) # split collection by coma
    print(str(int(i.split(',')[0]))) # type cast 1st column to int and print as string
    print(i.split(',')[1]) # print 2nd column (order date)
    print(i.split(',')[3]) # print 4th column (order status)

# to remove duplicates
s = set([])
for i in orders:
    s.add(i.split(',')[3])

print(s)
