def solution():
    dic = {}
    for index in range(len(strings) - len(find_word)+1):
        word = strings[index:index + len(find_word)]
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1

    return dic[find_word]


if __name__ == "__main__":
    for i in range(10):
        testcase = input()
        find_word = input()

        strings = input()
        print(f"#{i+1} {solution()}")