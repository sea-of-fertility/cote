T = int(input())
for i in range(1, T+1):
    list_a = list(map(int, input().split()))
    if list_a[0] > list_a[1]:
        a = ">"
    elif list_a[0] == list_a[1]:
        a = "="
    else:
        a = "<"
    print(f"#{i} {a}")