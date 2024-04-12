t = int(input())

for i in range(1, t + 1):
    string = input()
    print(string)
    print(string[::-1])
    if string == string[::-1]:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")
