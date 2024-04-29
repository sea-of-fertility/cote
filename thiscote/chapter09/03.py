import sys, heapq

INF = int(1e9)

input = sys.stdin.readline


def dijkstra():
    distance[c] = 0

    heap = []
    heapq.heappush(heap, (0, c))

    while heap:
        weight, node = heapq.heappop(heap)
        if distance[node] < weight:
            continue
        for index, value in enumerate(graph[node]):
            cur_weight = weight + value
            if cur_weight < distance[index]:
                distance[index] = cur_weight
                heapq.heappush(heap, (cur_weight, index))


if __name__ == "__main__":
    n, m, c = map(int, input().split())

    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight

    distance = [INF for _ in range(n + 1)]

    dijkstra()

    max_value = -1
    answer = 0
    for index, item in enumerate(distance):
        if item != INF and index != c:
            answer += 1
            max_value = max(max_value, item)

    print(answer, max_value)
    """
3 2 1
1 2 4
1 3 2
    """