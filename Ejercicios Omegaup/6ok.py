n = int(input())
t = 0
for i in range(n):
    b, p = map(int, input().split())
    t = t + (b * p)
print(t)
