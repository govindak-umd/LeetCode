class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        box_1 = []
        box_2 = []
        box_3 = []
        box_4 = []
        box_5 = []
        box_6 = []
        box_7 = []
        box_8 = []
        box_9 = []

        all_possible_box_1 = []
        all_possible_box_2 = []
        all_possible_box_3 = []
        all_possible_box_4 = []
        all_possible_box_5 = []
        all_possible_box_6 = []
        all_possible_box_7 = []
        all_possible_box_8 = []
        all_possible_box_9 = []

        def extractEachSquare(board):

            for row in range(9):
                if 0 <= row <= 2:
                    box_1.append(board[row][0:3])
                    box_2.append(board[row][3:6])
                    box_3.append(board[row][6:9])
                if 3 <= row <= 5:
                    box_4.append(board[row][0:3])
                    box_5.append(board[row][3:6])
                    box_6.append(board[row][6:9])
                if 6 <= row <= 8:
                    box_7.append(board[row][0:3])
                    box_8.append(board[row][3:6])
                    box_9.append(board[row][6:9])

            print(box_1)
            # print(box_2)
            # print(box_3)
            # print(box_4)
            # print(box_5)
            # print(box_6)
            # print(box_7)
            # print(box_8)
            # print(box_9)

        def checkPossibilities():
            all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            for pos in all_numbers:
                for i in range(3):
                    if pos not in box_1[0] and pos not in box_1[1] and pos not in box_1[
                        2] and pos not in all_possible_box_1:
                        all_possible_box_1.append(pos)
                    if pos not in box_2[0] and pos not in box_2[1] and pos not in box_2[
                        2] and pos not in all_possible_box_2:
                        all_possible_box_2.append(pos)
                    if pos not in box_3[0] and pos not in box_3[1] and pos not in box_3[
                        2] and pos not in all_possible_box_3:
                        all_possible_box_3.append(pos)
                    if pos not in box_4[0] and pos not in box_4[1] and pos not in box_4[
                        2] and pos not in all_possible_box_4:
                        all_possible_box_4.append(pos)
                    if pos not in box_5[0] and pos not in box_5[1] and pos not in box_5[
                        2] and pos not in all_possible_box_5:
                        all_possible_box_5.append(pos)
                    if pos not in box_6[0] and pos not in box_6[1] and pos not in box_6[
                        2] and pos not in all_possible_box_6:
                        all_possible_box_6.append(pos)
                    if pos not in box_7[0] and pos not in box_7[1] and pos not in box_7[
                        2] and pos not in all_possible_box_7:
                        all_possible_box_7.append(pos)
                    if pos not in box_8[0] and pos not in box_8[1] and pos not in box_8[
                        2] and pos not in all_possible_box_8:
                        all_possible_box_8.append(pos)
                    if pos not in box_9[0] and pos not in box_9[1] and pos not in box_9[
                        2] and pos not in all_possible_box_9:
                        all_possible_box_9.append(pos)
            print(all_possible_box_1)
            # print(all_possible_box_2)
            # print(all_possible_box_3)
            # print(all_possible_box_4)
            # print(all_possible_box_5)
            # print(all_possible_box_6)
            # print(all_possible_box_7)
            # print(all_possible_box_8)
            # print(all_possible_box_9)

        def findinRow(num, row):
            if num in row:
                return False
            return True

        def findinColumn(num, board, col):
            for idx in range(9):
                if num == board[idx][col]:
                    return False
            return True

        def findinSquare(num, square):
            for row_idx in range(3):
                if num in square[row_idx]:
                    return False
                else:
                    return True

        extractEachSquare(board)
        checkPossibilities()

