from random import randrange

n = int(input("Enter size of array: "))
a = []

for i in range (0, n):
    a.append(int(input()))

print(a) #

m = int(input("Enter positive M: "))
k = int(input("Enter negative K: "))

sizePos = randrange(0, m)

print(sizePos)

sizeNeg = randrange(k, 0)

print(sizeNeg)

checkArr = []
for i in range(k, 0):
    checkArr.append(i)

print(checkArr)


end = []
while(len(end)!=sizePos):
    temp = randrange(k, 0)
    if(temp in checkArr):
        end.append(temp)

print(end)
