n = int(input())

operators = {}

while n!=0:
    one = input()
    one = one.split(": ")
    operators[one[0]] = one[1]
    n = n - 1
    
print(operators)

num = int(input())

phoneNum = {}
while num!=0:
    number = input()
    number = number.split(": ")
    phoneNum[number[0]] = number[1]
    num = num - 1

randoms = int(input())

listrandoms = []
while randoms!=0:
    r = input()
    listrandoms.append(r)
    randoms = randoms - 1

if(listrandoms[0] in phoneNum):
    print("Yes")
else:
    print("No")
