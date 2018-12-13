import re

def parse(s):
    return [[*map(int, re.findall(r'-?\d+', l))] for l in s.splitlines()]

def plot(points):
    minx, maxx = min(p[0] for p in points), max(p[0] for p in points)
    miny, maxy = min(p[1] for p in points), max(p[1] for p in points)
    field = [[' ']*(maxx-minx+1) for _ in range(maxy-miny+1)]
    for x, y, _, _ in points:
        field[y-miny][x-minx] = '#'
    return '\n'.join(''.join(r) for r in field)

def converge(points, letter_height=12):
    i = 0
    while max(p[1] for p in points) - min(p[1] for p in points) > letter_height:
        for p in points:
            p[0] += p[2]
            p[1] += p[3]
        i += 1
    return i

points = parse(open('Advent10.txt').read())
part2 = converge(points)
print(plot(points))  # Part 1