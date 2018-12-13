A = [3, 2, 4, 1]
B = []

n = len(A)
while(n > 0):
    tempMin = 99999
    for i in range(0, len(A)):
        if (tempMin > A[i]):
            tempMin = A[i]
    B.append(tempMin)
    A.remove(tempMin)
    n = n - 1
print(B)

