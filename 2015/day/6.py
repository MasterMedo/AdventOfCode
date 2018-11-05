import numpy as np

f = {
        "turnon": lambda x, y: x * 1 + y,   # x * 1
        "turnoff": lambda x, y: x * -1 + y, # x * -1
        "toggle": lambda x, y: x * 2 + y    # 1 - y
    }

with open('../input/6.txt') as f:
    data = [i.replace("turn ", "turn").split() for i in f.readlines()]

grid = np.zeros((1000, 1000))
for line in data:
    x1, y1, x2, y2 = map(int, ''.join(line[1] + ',' + line[-1]).split(','))
    grid[x1: x2 + 1, y1: y2 + 1] = f[line[0]](np.ones((x2 - x1 + 1, y2 - y1 + 1)), grid[x1: x2 + 1, y1: y2 + 1])
    grid[grid < 0] = 0

print int(np.sum(grid))