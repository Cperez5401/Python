def countdown(num):
    for i in range(num, -1, -1):
        print(i)
countdown(5)
def printandReturn(list):
    print(list[0])
    return list[1]
print(printandReturn([1,2]))
def firstPlusLength(list):
    product = 0
    product = len(list) + list[0]
    return product
print(firstPlusLength([1,2,3,4,5,6]))
def valuesGreaterThan(list):
    if len(list)<2:
        return false
    newlist=[]
    for val in list:
        if val > list[1]:
            newlist.append(val)
    print(len(newlist))
    return newlist
print(valuesGreaterThan([55,6,2,3,99,78,20,1]))
print(valuesGreaterThan(([5,2,3,2,1,4])))
def thisLenVal(size,value):
    newlist = []
    for i in range(size):
        newlist.append(value)
    return newlist
print(thisLenVal(3, 8))


