n, m = map(int, input().split())
s = 0
for i in range(0, m):
    p = int(input())
    s = s + p
r = n - s
print(r)
