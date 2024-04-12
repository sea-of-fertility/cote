t = int(input())

for i in range(1, t + 1):
    word = input()
    for check in range(1, 30):
        if word[0:check] == word[check: check * 2]:
            answer: int = len(word[0:check])
        print(f"#{i} {answer}")
