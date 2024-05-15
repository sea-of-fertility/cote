import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline


def dijkstra():
    heap = []

    distance[1] = 0

    heapq.heappush(heap, (0, 1))

    while heap:
        weight, node = heapq.heappop(heap)
        if distance[node] < weight:
            continue

        for i in graph[node]:
            cur_distance = distance[node] + 1
            if cur_distance < distance[i]:
                distance[i] = cur_distance
                heapq.heappush(heap, (cur_distance, i))


if __name__ == "__main__":
    n, m = map(int, input().split())
    distance = [INF for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    dijkstra()

    distance = distance[1:]

    depth = max(distance)
    index = distance.index(depth)
    same_depth = distance.count(depth)
    print(index + 1, depth, same_depth)
"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

"""
