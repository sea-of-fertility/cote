def solution(a, b):
    if b == 1:
        return a
    return a * solution(a, b-1)


if __name__ == "__main__":

    t = int(input())

    for case in range(t):
        a, b = map(int, input().split())
        print(f"#{case+1} {solution(a, b)}")
