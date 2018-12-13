with open("Advent11.txt", "r") as f:
    serial_number = int(f.read())

def get_power_level(x, y):
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

max_total_power = 0
max_total_power_coords = (0, 0)

for y in range(1, 299):
    for x in range(1, 299):
        total_power = sum(sum(get_power_level(x+square_x, y+square_y) for square_x in range(3)) for square_y in range(3))
        if total_power > max_total_power:
            max_total_power = total_power
            max_total_power_coords = (x, y)

print(",".join(str(c) for c in max_total_power_coords))