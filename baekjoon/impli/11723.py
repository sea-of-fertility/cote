import sys

input = sys.stdin.readline

if __name__ == "__main__":
    m = int(input())
    data = set()
    for _ in range(m):
        order = input().split()
        if len(order) == 1:
            data = set(range(1, 21)) if order[0] == "all" else set()
        else:
            n = int(order[1])
            if order[0] == "add":
                data.add(n)
            elif order[0] == "remove":
                data.discard(n)
            elif order[0] == "check":
                print(1 if n in data else 0)
            elif order[0] == "toggle":
                data.discard(n) if n in data else data.add(n)
