T = int(input())

for i in range(1, T + 1):
    list_a = list(map(int, input().split()))
    answer = [x for x in list_a if x != min(list_a) if x != max(list_a)]
    answer = int(sum(answer) / len(answer) + 0.5)
    print(f"#{i} {answer}")