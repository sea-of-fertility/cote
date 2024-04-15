def solution(num):
    value = building[num] - max(building[num-1], building[num-2], building[num+2], building[num+1])
    return value if value > 0 else 0


if __name__ == "__main__":
    for i in range(10):
        answer = 0
        count = int(input())
        building = list(map(int, input().split()))
        for num in range(2, len(building)-2):
            answer += solution(num)
        print(f"#{i+1} {answer}")


