n, c = map(int, input().split())
sumaPred = 0
contPred = 0
if c > 0:
    for i in range(0, n):
        pred = int(input())
        sumaPred = sumaPred + pred
        if(sumaPred <= c):
            contPred += 1
print(contPred)


""" n, m = map(int, input().split())
s = 0
for i in range(0, m):
    p = int(input())
    s = s + p
r = n - s
print(r) """
