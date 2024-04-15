cnt = int(input())

data = []

for i in range(cnt):
    data.append(int(input()))

data.sort(reverse=True)

for d in data:
    print(d, end=" ")