from statistics import mode

f = open(r'input_3.txt', 'r')
rows = [row[:-1] for row in f]


# rows = [
#     '00100',
#     '11110',
#     '10110',
#     '10111',
#     '10101',
#     '01111',
#     '00111',
#     '11100',
#     '10000',
#     '11001',
#     '00010',
#     '01010',
# ]


def most_common(List):
    return(mode(List))


def gen_rows_map(length):
    return [[] for i in range(length)]


def fill_rows_map(rows_map, rows):
    for row in rows:
        for i in range(len(row)):
            rows_map[i] += row[i]


def find_rates(rows):
    rows_map = gen_rows_map(len(rows[0]))
    fill_rows_map(rows_map, rows)

    gamma_bin = ''.join([most_common(row) for row in rows_map])
    epsilon_bin = ''.join([str((int(n) + 1) % 2) for n in gamma_bin])

    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    return gamma * epsilon


print(find_rates(rows))
