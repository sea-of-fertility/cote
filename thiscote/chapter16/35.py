from collections import deque


def dp():
    answer = {1: True, 2: True, 3: True, 5: True}

    de = deque([1, 2, 3, 5])

    arr = [2, 3, 5]

    while de and len(answer) <= index:
        item = de.popleft()

        for a in arr:
            new_item = a * item
            if new_item not in answer:
                de.append(new_item)
                answer[new_item] = True

    return answer


if __name__ == "__main__":
    index = int(input())
    answer = dp()
    a = sorted(list(answer.keys()))
    print(a[index-1])
