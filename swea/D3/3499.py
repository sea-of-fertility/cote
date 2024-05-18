def solution():
    data = jud.count('x')
    if data >= 8:
        print(f"#{case+1} NO")
    else:
        print(f"#{case+1} YES")


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        jud = list(input())
        solution()
