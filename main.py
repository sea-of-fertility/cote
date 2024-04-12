# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def solution(park, routes):
    h = len(park)
    w = len(park[0])
    move = 0
    low = 0
    col = 0
    start = []

    for col in range(h):
        for low in range(w):
            if park[col][low] == 'S':
                print("위치:", col, low)
                start =[col, low]
                break
    col = start[0]
    low = start[1]
    print(col, low)

    for i in routes:
        where, move = i.split()
        move = int(move)
        print("움직임:", move)
        if where == 'E' and low + move < w and park[col][low + move] != 'X':
            low += move
        elif where == 'W' and low - move >= 0 and park[col][low - move] != 'X':
            low -= move
        elif where == 'S' and col + move < h and park[col + move][low] != 'X':
            col += move
        elif where == 'N' and col - move >= 0 and park[col - move][low] != 'X':
            col -= move
        print("이동", col, low)
    print(col, low)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution(["OOS","OXX","OOO"], ["E 2","S 2","W 1"])