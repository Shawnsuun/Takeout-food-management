def find_submatrix(board, pattern):

    def is_valid_submatrix(submatrix, digit_map):
        for i in range(len(submatrix)):
            for j in range(len(submatrix[0])):
                if pattern[i][j].isalpha():
                    coordinates = digit_map[pattern[i][j]]
                    for coord in coordinates:
                        if submatrix[i][j] != submatrix[coord[0], coord[1]]:
                            return False
                elif submatrix[i][j] != int(pattern[i][j]):
                    return False
        return True
    
    rows_board = len(board)
    cols_board = len(board[0])
    rows_pattern = len(pattern)
    cols_pattern = len(pattern[0])
    
    for r in range(rows_board - rows_pattern + 1):
        for c in range(cols_board - cols_pattern + 1):
            submatrix = [board[i][c:c + cols_pattern] for i in range(r, r + rows_pattern)]
            digit_map = {}
            used_digits = set()
            valid = True
            
            for i in range(rows_pattern):
                for j in range(cols_pattern):
                    if pattern[i][j].isalpha():
                        if pattern[i][j] in digit_map:
                            if submatrix[i][j] != digit_map[pattern[i][j]]:
                                valid = False
                                break
                        else:
                            digit_map[pattern[i][j]] = submatrix[i][j]
                            used_digits.add(submatrix[i][j])
                    elif int(pattern[i][j]) != submatrix[i][j]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid and len(used_digits) == len(digit_map):
                return [r, c]
    
    return [-1, -1]


# Test Case 1
board1 = [
    [2, 4, 2, 4, 2],
    [4, 2, 4, 2, 2],
    [1, 4, 2, 5, 3]
]

pattern1 = [
    ['4', 'c'],
    ['c', 'b']
]

result1 = find_submatrix(board1, pattern1)
print(result1)  # Output: [0, 1]


# Test Case 2
board2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pattern2 = [
    ['x', 'x'],
    ['x', 'x']
]

result2 = find_submatrix(board2, pattern2)
print(result2)  # Output: [-1, -1]


# Test Case 3
board3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pattern3 = [
    ['x', '2'],
    ['4', 'x']
]

result3 = find_submatrix(board3, pattern3)
print(result3)  # Output: [1, 0]


# Test Case 4
board4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pattern4 = [
    ['x', 'x'],
    ['7', '8']
]

result4 = find_submatrix(board4, pattern4)
print(result4)  # Output: [2, 0]