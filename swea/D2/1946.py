T = int(input())
for i in range(1, T + 1):
    ch = ''
    t = int(input())
    print(f"#{i}")
    for l in range(t):
        a, b = input().split()
        ch += a * int(b)

    answer = ''
    for a in ch:
        if len(answer) == 10:
            print(answer)
            answer = a

        else:
            answer += a
    if len(answer) != 0:
        print(answer)



