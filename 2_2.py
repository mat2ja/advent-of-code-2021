import numpy as np

f = open(r'input_2.txt', 'r')
rows = [row[:-1] for row in f]
courses = [tuple(row.split(' ')) for row in rows]

directionMap = {
  'forward': lambda x, prev_aim: (x, x * prev_aim, 0),
  'down': lambda aim, prev_aim: (0, 0, aim),
  'up': lambda aim, prev_aim: (0, 0, -aim),
}


def calc_course(courses):
  global_course = (0, 0, 0)
  for dir, value in courses:
    (prev_x, prev_y, prev_aim) = global_course
    step = directionMap[dir](int(value), int(prev_aim))
    global_course = tuple(np.add(global_course, step))

  x, y, aim = global_course
  return abs(x) * abs(y);


print(calc_course(courses))