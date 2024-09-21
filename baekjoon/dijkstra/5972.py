import heapq
import sys

INF = sys.maxsize


def dijkstra(n, graph):
    start = 1
    distance = [INF for _ in range(n+1)]
    distance[0] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        weight, destination = heapq.heappop(heap)
        if distance[destination] < weight:
            continue
        else:
            for value, node in graph[destination]:
                new_weight = value + weight
                if distance[node] > new_weight:
                    distance[node] = new_weight
                    heapq.heappush(heap, (new_weight, node))
    return distance

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]  # 정점의 개수에 맞게 n+1로 수정
    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    print(dijkstra(n, graph)[n])


if __name__ == "__main__":
    main()
