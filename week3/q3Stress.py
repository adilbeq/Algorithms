from random import randrange
import sys
while (True):
    
    minimum = 0
    A = []
    #m = int(input("Enter positive M: "))
    #N = randrange(0, m)
    N = 5
    k = -7
    
    checkArr = []
    for i in range(k, 0):
        checkArr.append(i)

    end = []
    while(len(A)!=N):
        temp = randrange(k, 0)
        if(temp in checkArr):
            A.append(temp)
    print(A)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if (A[i]!=A[j]) and (A[j]!=A[k]) and (A[i]!=A[k]):
                    if (A[i])**3 + (A[j])**3 + (A[k])**3 < minimum:
                        minimum = (A[i])**3 + (A[j])**3 + (A[k])**3
    print(minimum)
    #

    A.sort()
    min1 = A[0];
    min2 = A[1];
    min3 = A[2];
    last = (min1**3) + (min2**3) + (min3**3)
    print((min1**3) + (min2**3) + (min3**3))

    if(minimum != last):
        sys.exit("Error")
