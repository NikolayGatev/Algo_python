def is_out_inrange(row, col, matrix):
    return row >= len(matrix) or col >= len(matrix[0])


def is_visit(row, col, matrix):
    matrix[row][col] = 'v'


def find_all_paths(row, col, matrix):
    if is_out_inrange(row, col, matrix) or is_visit(row, col, matrix):
        return 0

    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return 1


    matrix[row][col] = 'v'
    result = 0

    result += find_all_paths(row + 1, col, matrix) # right
    result += find_all_paths(row, col + 1, matrix) # down

    matrix[row][col] = '-'

    return result




rows = int(input())
cols = int(input())
matrix = []
for r in range(rows):
    matrix.append(list('-' * cols))

print(find_all_paths(0, 0, matrix))