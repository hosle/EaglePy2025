# https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=hash-table

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


# start time 15:15
# finish time : 15:40
# Duration : 25min


def solution(board):

    columns = dict()
    rows = dict()
    cells = dict()

    for i in range(0, 9):
        for j in range(0, 9):
            current = board[i][j]

            if current == '.':
                continue
            else:
                column = columns.get(j, [])
                row = rows.get(i, [])
                index_cell = i//3 * 10 + j//3
                cell = cells.get(index_cell, [])

                if current in column or current in row or current in cell:
                    return False
                else:
                    column.append(current)
                    columns[j] = column

                    row.append(current)
                    rows[i] = row

                    cell.append(current)
                    cells[index_cell] = cell
    return True


def test_case1():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


    print("result = ", solution(board))
    assert solution(board) == True


def test_case2():
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print("result = ", solution(board))
    assert solution(board) == False

def test_case3():
    board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
             [".", "4", ".", "3", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "3", ".", ".", "1"],
             ["8", ".", ".", ".", ".", ".", ".", "2", "."],
             [".", ".", "2", ".", "7", ".", ".", ".", "."],
             [".", "1", "5", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "2", ".", ".", "."],
             [".", "2", ".", "9", ".", ".", ".", ".", "."],
             [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    print("result = ", solution(board))
    assert solution(board) == False


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()







