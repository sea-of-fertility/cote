import sys
from collections import defaultdict

input = sys.stdin.readline

book_dict = defaultdict(int)
cnt = int(input())
for i in range(cnt):
    b_name = input().strip()
    book_dict[b_name] += 1

best_seller = [ key for key, value in book_dict.items() if value == max(book_dict.values())]
best_seller.sort()
print(best_seller[0])