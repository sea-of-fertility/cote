T = int(input())
for i in range(1, T + 1):
    junk = int(input())
    list_a = list(map(int, input().split()))
    list_a.sort()
    print(f"#{i},end=" "")
    for case in range(len(list_a)):
        print(f"{case} ,end=""")
    print()


