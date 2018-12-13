class Cart:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.turn = 0
        self.crashed = False


carts, tracks = [], {}
for y, line in enumerate(open('Advent13.txt')):
    for x, char in enumerate(line):
        if char in ">v<^":
            if char == ">":
                direction = complex(1, 0)
            elif char == "v":
                direction = complex(0, 1)
            elif char == "<":
                direction = complex(-1, 0)
            elif char == "^":
                direction = complex(0, -1)
            else:
                print("Error 22: ?")
            carts.append(Cart(complex(x, y), direction))
        elif char in "\\/+":
            tracks[complex(x, y)] = char

first_crash = True
while len(carts) > 1:
    carts.sort(key=lambda c: (c.position.real, c.position.imag))
    for c1, cart in enumerate(carts):
        if cart.crashed:
            continue
        cart.position += cart.direction
        for c2, cart2 in enumerate(carts):
            if cart.position == cart2.position and c1 != c2 and not cart2.crashed:
                if first_crash:
                    print("1: %d,%d" % (cart.position.real, cart.position.imag))
                    first_crash = False
                cart.crashed = True
                cart2.crashed = True
        if cart.position in tracks:
            track = tracks[cart.position]
            if track == "\\":
                if cart.direction.real != 0:
                    cart.direction *= complex(0, 1)
                else:
                    cart.direction *= complex(0, -1)
            elif track == "/":
                if cart.direction.real != 0:
                    cart.direction *= complex(0, -1)
                else:
                    cart.direction *= complex(0, 1)
            elif track == "+":
                if cart.turn == 0:
                    cart.direction *= complex(0, -1)
                elif cart.turn == 1:
                    pass
                else:
                    cart.direction *= complex(0, 1)
                cart.turn = (cart.turn + 1) % 3
            else:
                print("Error 62: ?")
    carts = [cart for cart in carts if not cart.crashed]
print("2: %d,%d" % (carts[0].position.real, carts[0].position.imag))