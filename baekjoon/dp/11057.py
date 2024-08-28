def main():
    n = int(input())
    dp = [[] for _ in range(3)]
    dp[1] = [1 for _ in range(11)]
    dp[1].append(10)
    dp[2] = [value for value in range(10, 0, -1)]
    dp[2].append(55)
    for index in range(3, 1001):
        arr = [0 for _ in range(11)]
        arr[0] = dp[index-1][-1]
        for cnt in range(1, 10):
            arr[cnt] = arr[cnt-1] - dp[index-1][cnt-1]
        arr[10] = sum(arr[0:10])
        dp.append(arr)
    print(dp[n][-1] % 10007)


if __name__ == "__main__":
    main()