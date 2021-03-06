# Answer pending, will be completed at a later date.

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

        all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

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

            # print(box_1)
            # print(box_2)
            # print(box_3)
            # print(box_4)
            # print(box_5)
            # print(box_6)
            # print(box_7)
            # print(box_8)
            # print(box_9)

        def checkPossibilities():

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
            # print(all_possible_box_1)
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
                return True
            return False

        def findinColumn(num, board, col):
            for idx in range(9):
                if num == board[idx][col]:
                    return True
            return False

        def findinSquare(num, square):
            for row_idx in range(3):
                if num in square[row_idx]:
                    return True
                else:
                    return False

        def checkAllFilled(board):
            for row_idx in range(9):
                for col_idx in range(9):
                    if board[row_idx][col_idx] == '.':
                        return True
            return False

        def completeSquare(box):
            box_list = box[-3:]
            flat_list = []

            for sublist in box_list:
                for item in sublist:
                    flat_list.append(item)
            c = '.'
            matches = [x for x in flat_list if x == c]
            row = 0
            col = 0
            if len(matches) == 1:
                for row in range(3):
                    for col in range(3):
                        if box_list[row][col] == c:
                            idx = flat_list.index(c)
                            for i in all_numbers:
                                if i not in flat_list:
                                    if (box == box_1):
                                        print('Found in box_1 .. ')
                                        board[row][col] = i
                                    elif (box == box_4):
                                        print('Found in box_4 .. ')
                                        board[row + 3][col] = i
                                    elif (box == box_7):
                                        print('Found in box_7 .. ')
                                        board[row + 6][col] = i

                                    elif (box == box_2):
                                        print('Found in box_2 .. ')
                                        board[row][col + 3] = i
                                    elif (box == box_5):
                                        print('Found in box_5 .. ')
                                        board[row + 3][col + 3] = i
                                    elif (box == box_8):
                                        print('Found in box_8 .. ')
                                        board[row + 6][col + 3] = i

                                    elif (box == box_3):
                                        print('Found in box_3 .. ')
                                        board[row][col + 6] = i
                                    elif (box == box_6):
                                        print('Found in box_6 .. ')
                                        board[row + 3][col + 6] = i
                                    else:
                                        print('Found in box_9.. ')
                                        board[row + 6][col + 6] = i

        extractEachSquare(board)
        checkPossibilities()
        solved = False

        all_filled = checkAllFilled(board)
        curr_len = 0
        past_len = 0
        check = True

        while check == True:
            filledNumDic = {}

            for row_idx in range(9):
                for col_idx in range(9):
                    if board[row_idx][col_idx] == '.':
                        filledNumDic[(row_idx, col_idx)] = []

            real_board = board

            for row_idx in range(9):
                for col_idx in range(9):
                    if row_idx < 3 and col_idx < 3:
                        for num in all_possible_box_1:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_1) == False) and (
                                    box_1[row_idx][col_idx] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)
                    elif row_idx < 3 and 3 <= col_idx < 6:

                        for num in all_possible_box_2:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_2) == False) and (
                                    box_2[row_idx][col_idx - 3] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)

                    elif row_idx < 3 and 6 <= col_idx < 9:
                        for num in all_possible_box_3:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_3) == False) and (
                                    box_3[row_idx][col_idx - 6] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # print('success > ',num)
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)

                    elif 3 <= row_idx < 6 and col_idx < 3:
                        for num in all_possible_box_4:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_4) == False) and (
                                    box_4[row_idx - 3][col_idx] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)
                    elif 3 <= row_idx < 6 and 3 <= col_idx < 6:
                        for num in all_possible_box_5:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_5) == False) and (
                                    box_5[row_idx - 3][col_idx - 3] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)
                    elif 3 <= row_idx < 6 and 6 <= col_idx < 9:
                        for num in all_possible_box_6:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_6) == False) and (
                                    box_6[row_idx - 3][col_idx - 6] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)

                    elif 6 <= row_idx < 9 and col_idx < 3:
                        for num in all_possible_box_7:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_7) == False) and (
                                    box_7[row_idx - 6][col_idx] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)
                    elif 6 <= row_idx < 9 and 3 <= col_idx < 6:
                        for num in all_possible_box_8:
                            if (findinRow(num, board[row_idx]) == False) and (
                                    findinColumn(num, board, col_idx) == False) and (
                                    findinSquare(num, box_8) == False) and (
                                    box_8[row_idx - 6][col_idx - 3] not in all_numbers) and (
                                    num not in filledNumDic[(row_idx, col_idx)]):
                                # board[row_idx][col_idx] = num
                                filledNumDic[(row_idx, col_idx)].append(num)
                    elif 6 <= row_idx < 9 and 6 <= col_idx < 9:
                        for num in all_possible_box_9:
                            try:
                                if (findinRow(num, board[row_idx]) == False) and (
                                        findinColumn(num, board, col_idx) == False) and (
                                        findinSquare(num, box_9) == False) and (
                                        box_9[row_idx - 6][col_idx - 6] not in all_numbers) and (
                                        num not in filledNumDic[(row_idx, col_idx)]):
                                    # board[row_idx][col_idx] = num
                                    # pass
                                    filledNumDic[(row_idx, col_idx)].append(num)
                            except:
                                pass
            extractEachSquare(board)
            keys_to_be_deleted = []
            while (keys_to_be_deleted == []):
                for k, v in filledNumDic.items():
                    if len(v) == 1:
                        board[k[0]][k[1]] = v[0]
                        keys_to_be_deleted.append(k)
                for k in keys_to_be_deleted:
                    del filledNumDic[k]
                curr_len = len(filledNumDic)
                if past_len != curr_len:
                    print('Checking for single element left .. ')
                    completeSquare(box_1)
                    completeSquare(box_2)
                    completeSquare(box_3)
                    completeSquare(box_4)
                    completeSquare(box_5)
                    completeSquare(box_6)
                    completeSquare(box_7)
                    completeSquare(box_8)
                    completeSquare(box_9)
                    past_len = curr_len
                else:
                    check = False
                    break




