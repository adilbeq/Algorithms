#A = [4, 1, 3, 2]
#A = [1, 2, 3, 4] # smallest number of inversions, when array is sorted
A = [6, 5, 4, 3, 2, 1] # largest number of inversion, when array is sorted(reversed) descending order
cnt = 0 
for i in range(len(A)):
    for j in range(len(A)):
        if(i < j):
            if(A[i] > A[j]):
                cnt = cnt + 1
print(cnt)
