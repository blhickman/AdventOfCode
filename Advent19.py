lines = open("Advent19.txt", "r").readlines()
a, b = int(lines[22].split()[2]), int(lines[24].split()[2])
n1 = 836 + a * 22 + b
n2 = n1 + 10550400

print(sum(d for d in range(1, n1 + 1) if n1 % d == 0))
print(sum(d for d in range(1, n2 + 1) if n2 % d == 0))