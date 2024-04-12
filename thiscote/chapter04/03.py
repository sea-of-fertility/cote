import sys

input = sys.stdin.readline

look = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def set_look(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    else:
        return 2


def solution(map_size, start_point, game_map):
    look_point = start_point[-1]

    curren_point = start_point[0:-1]

    cnt = 4
    while cnt != 0:
        dx = curren_point[1] + look[look_point][1]
        dy = curren_point[0] + look[look_point][0]
        if map_size[1] > dx >= 0 == game_map[dy][dx] and 0 <= dy < map_size[0]:
            curren_point[1] = dx
            curren_point[0] = dy
            look_point = set_look(look_point)
            game_map[dy][dx] = 1

        else:
            look_point = set_look(look_point)


if __name__ == '__main__':
    map_size = list(map(int, input().split()))

    start_point = list(map(int, input().split()))

    game_map = []

    for i in range(map_size[0]):
        game_map.append(input().split())
    solution(map_size, start_point, game_map)
