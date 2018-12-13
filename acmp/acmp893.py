import math
f = open('INPUT.txt', 'r')
s = f.read()
n = int(s)
fn = math.factorial(n)
k = n - 3
fk = math.factorial(k)
res = fn // fk
res = str(res)
r = open("OUTPUT.txt", "w")
r.write(res)
r.close()
f.close()
