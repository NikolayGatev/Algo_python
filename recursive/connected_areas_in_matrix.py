class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def is_wall_or_visit(row, col, matrix):
    return matrix[row][col] != '-'


def out_inrange(row, col, matrix):
    return not (0 <= row < len(matrix) and 0 <= col < len(matrix[0]))


def explore_area(row, col, matrix):
    if out_inrange(row, col, matrix):
        return 0
    if is_wall_or_visit(row, col, matrix):
        return 0
    matrix[row][col] = 'v'
    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result

rows = int(input())
cols = int(input())
matrix = []


for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for index, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}')
