
import heapq

INF = int(1e9)


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, nodes + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra():
    visited[start] = True
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cur_dist, node = heapq.heappop(heap)
        if distance[node] < cur_dist:
            continue

        for index, weight in enumerate(graph[node]):
            total = cur_dist + weight
            if total < distance[index]:
                distance[index] = total
                heapq.heappush(heap, (total, index))


if __name__ == "__main__":

    nodes, edge = map(int, input().split())
    start = int(input())
    graph = [[INF for i in range(nodes + 1)] for _ in range(nodes + 1)]

    visited_order = []

    visited = [False for _ in range(nodes + 1)]
    distance = [INF for i in range(nodes + 1)]

    for _ in range(edge):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    dijkstra()
    print(visited_order)

    for i in range(1, nodes + 1):
        print(f"distance: {distance[i]}") if distance[i] != INF else print("no path")

"""
=== sample ===


6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

"""
