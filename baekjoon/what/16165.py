import sys

girl_group_dict = {}
members_group = {}

group_count, quiz_count = map(int, sys.stdin.readline().split())
for _ in range(group_count):
    group = sys.stdin.readline().strip()
    girl_group_dict[group] = []
    members = int(sys.stdin.readline().strip())
    member_list = []
    for member in range(members):
        name = sys.stdin.readline().strip()
        members_group[name] = group
        member_list.append(name)
    member_list.sort()
    girl_group_dict[group] = member_list

for quiz in range(quiz_count):
    data = sys.stdin.readline().strip()
    quiz_type = int(sys.stdin.readline().strip())
    if quiz_type == 1:
        print(members_group[data])
    else:
        for i in girl_group_dict[data]:
            print(i)