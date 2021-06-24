#1
for x in range(151):
    print(x)
for x in range (5, 1001, 5):
    print(x)
#2
for x in range (101):
    if x % 5 == 0:
        print("coding")
        if x % 10 == 0:
            print("Dojo")
    else:
        print(x)
#3
sum = 0
for x in range(1, 500001):
    if x % 2 != 0:
        sum =sum + x
print(sum)
#4
for x in range(2018, -1, -4):
    print(x)
#5
def flex_countdown(low, high, mult):
    for x in range(low, high+1):
        if x % mult == 0:
            print(x)
flex_countdown(2, 9, 3)



