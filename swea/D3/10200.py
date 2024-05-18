def solution():
    max_sub = min(a, b)
    c = a + b - n
    min_sub = c if c > 0 else 0
    return  max_sub, min_sub


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n, a, b = map(int, input().split())
        max_sub, min_sub = solution()
        print(f"#{case + 1} {max_sub} {min_sub}")
"""

3
10 3 5
10 7 5
100 100 100
"""
