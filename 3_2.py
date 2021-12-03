f = open(r'input_3.txt', 'r')
rows = [row[:-1] for row in f]


def gen_rows_map(rows):
    rows_map = [[] for i in range(len(rows[0]))]
    for row in rows:
        for i in range(len(row)):
            rows_map[i] += row[i]
    return rows_map


def calc_oxygen_rate(rows, rows_map_og):
    rows_map = rows_map_og[:]
    filt_rows = rows[:]

    for i in range(len(rows_map)):
        rows_map = gen_rows_map(filt_rows)

        if (len(filt_rows) == 1):
            break

        mc = '1' if rows_map[i].count('1') >= rows_map[i].count('0') else '0'
        filt_rows = [row for row in filt_rows if row[i] == mc]

    result = ''.join(filt_rows)
    return int(result, 2)


def calc_co2_rate(rows, rows_map_og):
    rows_map = rows_map_og[:]
    filt_rows = rows[:]

    for i in range(len(rows_map)):
        rows_map = gen_rows_map(filt_rows)
        if (len(filt_rows) == 1):
            break

        lc = '0' if rows_map[i].count('1') >= rows_map[i].count('0') else '1'
        filt_rows = [row for row in filt_rows if row[i] == lc]

    result = ''.join(filt_rows)
    return int(result, 2)


def calc_life_support(rows):
    rows_map = gen_rows_map(rows)

    oxygen = calc_oxygen_rate(rows, rows_map)
    co2 = calc_co2_rate(rows, rows_map)

    return oxygen * co2


print(calc_life_support(rows))
