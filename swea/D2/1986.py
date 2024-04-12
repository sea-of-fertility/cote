t = int(input())

for i in range(1, t+1):
    num = int(input())
    answer = []
    for x in range(1, num+1):
        if x % 2 == 0:
            answer.append(-x)
        else:
            answer.append(x)
        print(f"#{i} {sum(answer)}")