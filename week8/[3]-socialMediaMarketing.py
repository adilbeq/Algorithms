S = 2000
F = [100, 150] #followers
M = [10000, 1500] #cost (money)
FK = [] # cost for one follower
for i in range(len(F)):
    frack = M[i] // F[i]
    FK.append(frack)

cnt = 0
ans = 0

while(cnt != S):
    minFK = FK.index(min(FK))
    if(F[minFK] != 0):
        cnt = cnt + FK[minFK]
        F[minFK] = F[minFK] - 1
        ans = ans + 1
    if(F[minFK] == 0):
        FK[minFK] = 99999
        
print(ans)
