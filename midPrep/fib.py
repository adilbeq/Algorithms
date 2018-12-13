def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))


memo = []
def fibDP(n):
    if n in memo:
        return memo[n]
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

#print(fibDP(6))


def Fib2(n):
    F = []
    for i in range(0, n+1):
        F.append(0)
    F[0] = 0
    F[1] = 1
    for i in range(2, n):
        F[i] = F[i-1] + F[i-2]
    return F[n]

print(Fib2(6))
