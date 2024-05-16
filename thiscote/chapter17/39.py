import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]



def solution():
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while heap:
        heappop = heapq.heappop(heap)
        weight = heappop[0]
        y = heappop[1]
        x = heappop[2]

        for m in range(4):
            c_y = dy[m] + y
            c_x = dx[m] + x
            if 0 <= c_y < n and 0 <= c_x < n:
                value = weight + graph[c_y][c_x]
                if distance[c_y][c_x] < graph[c_y][c_x]:
                    continue

                if value < distance[c_y][c_x]:
                    distance[c_y][c_x] = value
                    heapq.heappush(heap, (value, c_y, c_x))


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        distance = [[INF for _ in range(n)] for _ in range(n)]
        graph = [list(map(int, input().split())) for _ in range(n)]

        solution()
        print(distance[n-1][n-1])



"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3 
0 7 6 1 6 8 5
1 1 7 8 3 2 3 
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""