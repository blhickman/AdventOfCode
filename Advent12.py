with open('Advent12.txt', 'r') as f:
    _, _, init = next(f).strip().split()
    next(f)
    rules = dict()
    for line in f:
        x, _, y = line.strip().split()
        rules[x] = y


def solve(gen):
    hist = dict()
    state = init
    idx = 0
    while gen:
        gen -= 1
        state = '....' + state + '....'  # assuming that '.....' => '.'
        idx -= 2  # if '....#' => '#' then the state grows to the left by two
        newstate = ''
        while len(state) > 4:
            c = rules[state[:5]]
            if newstate == '' and c == '.':  # omit leading zeroes
                idx +=1
            else:
                newstate += c
            state = state[1:]
        state = newstate
        while state[-1] == '.':  # remove trailing zeroes
            state = state[:-1]
        if state in hist:  # found a recurrance - skip cycles
            prev_idx, prev_gen = hist[state]
            dg = prev_gen - gen
            idx += gen // dg  * (idx - prev_idx)
            gen = gen % dg
            hist = dict()  # we won't be cycling from now anyway, so avoid unnecessary searching
        else:
            hist[state] = (idx, gen)

    return sum(idx + i for i, c in enumerate(state) if c == '#')


print("Part 1:", solve(20))
print("Part 2:", solve(50000000000))