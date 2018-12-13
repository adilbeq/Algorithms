def average(S):
    cnt = 0
    for i in S:
        cnt = cnt + i
    cnt = cnt / (len(S))
    return cnt

print(average([1,2,3,4]))
