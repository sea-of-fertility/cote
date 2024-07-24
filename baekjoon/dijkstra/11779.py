import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline

def solution(s, e):
    distance = [INF for _ in range(n+1)]
    distance[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    global visit

    while heap:
        w, node = heapq.heappop(heap)

        if distance[node] < w:
            continue

        for new_w, new_node in graph[node]:
            cur_weight = new_w + w
            if cur_weight < distance[new_node]:
                distance[new_node] = cur_weight
                heapq.heappush(heap, (cur_weight, new_node))
                visit[new_node] = node
    return distance[e]


def find(s, e):
    answer = [e]
    while e != 0:
        e = visit[e]
        answer.append(e)
    return answer[:-1]


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append([weight, end])
    result_start, result_end = map(int, input().split())
    visit = [0 for _ in range(n+1)]
    answer1 = solution(result_start, result_end)
    print(answer1)
    l = find(result_start, result_end)
    print(len(l))
    for item in l[::-1]:
        print(item, end=" ")
