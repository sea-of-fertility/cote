import sys

input = sys.stdin.readline

password_dict = dict()
n, m = map(int, input().split())
for cnt in range(1, n+1):
    site, password = input().split()
    password_dict[site] = password
for _ in range(m):
    site = input().strip()
    print(password_dict[site])
