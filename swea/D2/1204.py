T = int(input())
for i in range(1, T + 1):
    a = int(input())
    list_a = list(map(int, input().split()))
    score_list = [0 for x in range(101)]

    for score in list_a:
        score_list[score] += 1
    mode = max(score_list)
    answer = 0
    for index, value in enumerate(score_list):
        if value == mode:
            answer = index
    print(f"#{i} {answer}")

