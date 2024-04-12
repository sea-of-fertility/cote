def solution(n, lost, reserve):
    cnt = 0
    for num in lost:
        if num + 1 in reserve:
            reserve.remove(num + 1)
            lost.remove(num)

        elif num - 1 in reserve:
            reserve.remove(num - 1)
            lost.remove(num)
        else:
            cnt += 1
    return n - (cnt + len(lost))


if __name__ == '__main__':
    i = solution(5, [2, 4], [1, 3, 5])