def biggieSize(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i]= "Big"
    return list
print(biggieSize([-1, 3, 5, -5]))
def countPositive(list):
    count = 0
    for i in range(len(list)):
        if list[i]> 0:
            count += 1
    list[len(list) - 1] = count
    return list
print(countPositive([-1,1,1,1]))
def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
print(sumTotal([1,2,3,4]))
def average(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = sum / len(list)
    return average
print(average([1,2,3,4]))
def length(list):
    return len(list)
print(length([37,2,1,-9]))
def minVal(list):
    return(min(list))
print(minVal([37,2,1,-9]))
def maxVal(list):
    return(max(list))
print(maxVal([37,2,1,-9]))
def ultimate_analysis(array):
    myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for val in array:
        if myDictonary['minimum']<val:
            myDictonary['minimum'] = val
        if myDictonary['maximun']>val:
            myDictonary['maximun'] = val
        myDictonary['sumTotal']+= val
        myDictonary['average']=myDictonary['sumTotal']/len(array)
    return myDictonary
print(ultimate_analysis([1,2,1,2,4,0]))
def reverse_list(array):
    for i in range(0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array
print(reverse_list([11,12,13]))
def reverse_list(array):
    for i in range(0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array
print(reverse_list([11,12,13]))
