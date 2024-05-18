import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)

        if distance[node] < weight:
            continue

        for value, connect_node in graph[node]:
            total_weight = weight + value
            if total_weight < distance[connect_node]:
                distance[connect_node] = total_weight
                heapq.heappush(heap, (total_weight, connect_node))


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    start, end_point = map(int, input().split())
    solution()
    print(distance[end_point])