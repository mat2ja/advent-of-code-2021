'''
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.
'''

f = open(r'1_input.txt', 'r')
rows = [int(row[:-1]) for row in f]


def count_increases_triples(rows):
    count = 0
    for i in range(3, len(rows)):

        sum_prev = sum([rows[i-1], rows[i-2], rows[i-3]])
        sum_curr = sum([rows[i], rows[i-1], rows[i-2]])

        if (sum_curr > sum_prev):
            count += 1
    return count


print(count_increases_triples(rows))  # 1597

# test = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263,
# ]

# print(count_increases_triples(test)) # 5
