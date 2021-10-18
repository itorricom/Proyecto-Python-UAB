n = int(input())
altura = list(map(int, input().split()))
altura.sort()
print(altura)
for i in altura:
    if i == i+1:

