def is_correct_direction( row, coll, lab):
    return 0 <= row and 0 <= coll and coll < len(lab[0]) and row < len(lab) and lab[row][coll] != '*' and lab[row][coll] != 'v'

def find_all_paths(row, coll, lab, direction, path):
    if not is_correct_direction(row, coll, lab):
        return

    path.append(direction)

    if lab[row][coll] == 'e':
        print(''.join(path))
    else:
        lab[row][coll] = 'v'
        find_all_paths(row + 1, coll, lab, 'D', path)
        find_all_paths(row - 1, coll, lab, 'U', path)
        find_all_paths(row, coll +1, lab, 'R', path)
        find_all_paths(row, coll - 1, lab, 'L', path)

        lab[row][coll] = '-'
    path.pop()

rows = int(input())
colls = int(input())

lab = []
for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, '', [])