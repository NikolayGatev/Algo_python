def print_board(board):
    for row in board:
        print(' '.join(row))
        print()

def can_place_queen(row, coll, rows, colls, left_diagonals, right_diagonals):
    if row in rows:
        return False
    if coll in colls:
        return False
    if (row - coll) in left_diagonals:
        return False
    if (row + coll) in right_diagonals:
        return False
    return True

def set_queen(row, coll, board, rows, colls, left_diagonals, right_diagonals):
    board[row][coll] = '*'
    rows.add(row)
    colls.add(coll)
    left_diagonals.add(row - coll)
    right_diagonals.add(row + coll)

def remove_quens(row, coll, board, rows, colls, left_diagonals, right_diagonals):
    board[row][coll] = '-'
    rows.remove(row)
    colls.remove(coll)
    left_diagonals.remove(row - coll)
    right_diagonals.remove(row + coll)

def put_queens(row, board, rows, colls, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return

    for coll in range(8):
       if can_place_queen(row, coll, rows, colls, left_diagonals, right_diagonals):
           set_queen(row, coll, board, rows, colls, left_diagonals, right_diagonals)
           put_queens(row + 1, board, rows, colls, left_diagonals, right_diagonals)
           remove_quens(row, coll, board, rows, colls, left_diagonals, right_diagonals)


n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]

put_queens(0, board, set(), set(), set(), set())