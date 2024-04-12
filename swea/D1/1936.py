a, b = map(int, input().split())

if abs(a-b) < 2:
    if a-b > 0:
        print('A')
    else:
        print('B')
else:
    if a-b < 0:
        print('A')
    else:
        print('B')