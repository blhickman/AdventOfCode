import numpy

with open("Advent11.txt", "r") as f:
    serial_number = int(f.read())

def get_power_level(x, y):
    x += 1
    y += 1
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfunction.html
matrix = numpy.fromfunction(get_power_level, (300, 300), dtype=int)
max_total_power = (0, 0, 0, 0)

for y in range(300):
    for x in range(300):
        max_size = min([300-y, 300-x])
        for size in range(1, max_size+1):
            total_power = numpy.sum(matrix[x:x+size, y:y+size])
            if total_power > max_total_power[0]:
                max_total_power = (total_power, x+1, y+1, size)

print(",".join(str(x) for x in max_total_power[1:]))