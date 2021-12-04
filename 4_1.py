import re

# f = open(r'input_4.txt', 'r')
f = open(r'input_4.txt', 'r')
rows = [row[:-1].split('\n\n') for row in f]


def exractBoardRow(board_lines, j):
    return [int(ch) for ch in re.split(
        '\s+', board_lines[j][0]) if ch != '']


# create boards
def setup_game(rows):
    draws = [int(n) for n in rows[0][0].split(',')]

    board_lines = rows[1:]
    board_lines = [line for line in board_lines if line[0] != '']

    boards = []
    for i in range(0, len(board_lines), 5):
        board = [exractBoardRow(board_lines, j) for j in range(i, i+5)]
        boards += [board]

    return (draws, boards)


def store_rows(boards):
    # store board rows
    board_dict_rows = {}
    for key in range(len(boards)):
        for line in boards[key]:
            if key in board_dict_rows:
                board_dict_rows[key] += [line]
            else:
                board_dict_rows[key] = [line]
    return board_dict_rows


def store_cols(boards):
    # store board columns
    board_dict_cols = {}
    for key in range(len(boards)):
        columns = []
        for j in range(0, len(boards[key])):
            column = [row[j] for row in boards[key]]
            columns += [column]
        board_dict_cols[key] = columns
    return board_dict_cols


def find_draw(draw, board_rows, board_cols):
    # board, last n
    bingo_tup = (None, None)

    for key in board_rows:
        for i in range(len(board_rows[key])):
            board_rows[key][i] = [
                n for n in board_rows[key][i] if n != draw]

            if not len(board_rows[key][i]):
                bingo_tup = (board_rows[key], draw)

        for key in board_cols:
            for i in range(len(board_cols[key])):
                board_cols[key][i] = [
                    n for n in board_cols[key][i] if n != draw]

                if not len(board_cols[key][i]):
                    bingo_tup = (board_cols[key], draw)

    return bingo_tup


def get_bingo_score(boards, draws):
    board_rows = store_rows(boards)
    board_cols = store_cols(boards)

    score = None
    for draw in draws:
        (board, final_draw) = find_draw(draw, board_rows, board_cols)

        if board:
            flat_list = [item for sublist in board for item in sublist]
            suma = sum(flat_list)

            score = suma * final_draw
            break

    return score


def calc_bingo(rows):
    (draws, boards) = setup_game(rows)
    return get_bingo_score(boards, draws)


print(calc_bingo(rows))  # 33462
