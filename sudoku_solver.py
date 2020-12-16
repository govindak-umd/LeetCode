class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        def extractEachSquare(board):
            box_1 = []
            box_2 = []
            box_3 = []
            box_4 = []
            box_5 = []
            box_6 = []
            box_7 = []
            box_8 = []
            box_9 = []

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
            print(box_2)
            print(box_3)
            print(box_4)
            print(box_5)
            print(box_6)
            print(box_7)
            print(box_8)
            print(box_9)

        extractEachSquare(board)

    def findinRow(num):
        pass

    def findinColumn(num):
        pass

    def findinSquare(num):
        for i in range(3):
            for j in range(3):
                pass

