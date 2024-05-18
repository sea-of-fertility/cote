import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline


def dijkstra():
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)
        if distance[node] < weight:
            continue

        for value, index in graph[node]:
            new = weight + value
            if new < distance[index]:
                heapq.heappush(heap, (new, index))
                distance[index] = new


if __name__ == "__main__":
    nodes, edge = map(int, input().split())
    start = int(input())
    distance = [INF for _ in range(nodes + 1)]
    graph = [[] for _ in range(nodes + 1)]
    for _ in range(edge):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    dijkstra()


    for i in distance[1:]:
        if i == INF:
            print("INF")
        else:
            print(i)
