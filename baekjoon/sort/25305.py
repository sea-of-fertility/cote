if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split())).sort(reverse=True)
    print(arr[m-1])

