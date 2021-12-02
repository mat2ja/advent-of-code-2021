'''
Count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)
'''

f = open(r'input_1.txt', 'r')
rows = [int(row[:-1]) for row in f]


def count_increases(rows):
    count = 0
    for i in range(1, len(rows)):
        if (rows[i] > rows[i-1]):
            count += 1
    return count


print(count_increases(rows))  # 1552
