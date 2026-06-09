class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seenrow = set()
            for number in row:
                if number != ".":
                    if number in seenrow:
                        return False
                    seenrow.add(number)
        for col in range(9):
            seencol = set()
            for row in range(9):
                number = board[row][col]
                if number != ".":
                    if number in seencol:
                        return False
                    seencol.add(number)
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seenbox = set()
                for r in range(3):
                    for c in range(3):
                        number = board[box_row + r][box_col + c]
                        if number != ".":
                            if number in seenbox:
                                return False
                            seenbox.add(number)
        return True