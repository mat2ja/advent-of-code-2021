import numpy as np

f = open(r'input_2.txt', 'r')

rows = [row[:-1] for row in f]
courses = [tuple(row.split(' ')) for row in rows]


directionMap = {
  'forward': lambda x: (x, 0),
  'down': lambda x: (0, x),
  'up': lambda x: (0, -x),
}

def calc_course(courses):
  global_course = (0, 0)
  for dir, value in courses:
    step = directionMap[dir](int(value))
    global_course = tuple(np.add(global_course, step))

  x, y = global_course
  return abs(x) * abs(y);


print(calc_course(courses))