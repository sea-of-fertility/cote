import sys


input = sys.stdin.readline



def dp_init(m):
    dp_table = [0 for _ in range(m + 1)]
    dp_table[0] = 1  # 0원을 만드는 경우의 수는 1로 초기화
    return dp_table


def solution(coin_list, m):
    dp_table = dp_init(m)

    for coin in coin_list:
        for col in range(coin, m + 1):
            dp_table[col] += dp_table[col - coin]  # 동전 사용 여부에 따른 경우의 수 갱신

    print(dp_table[m])  # m원을 만들 수 있는 경우의 수 출력


def main():
    test = int(input())
    for _ in range(test):
        a = int(input())  # 동전의 개수
        coin_list = list(map(int, input().split()))  # 동전 리스트
        m = int(input())  # 목표 금액
        solution(coin_list, m)


if __name__ == "__main__":
    main()
