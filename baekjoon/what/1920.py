input()
list_a = list(map(int, input().split()))
dic_a = {key: True for key in list_a}

input()
list_b = list(map(int, input().split()))

for i in list_b:
    if i in dic_a:
        print(1)
    else:
        print(0)
