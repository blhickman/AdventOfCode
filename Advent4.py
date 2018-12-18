from functools import partial
import numpy as np
from collections import defaultdict
import re

def Input(day):
    return open('Advent4.txt'.format(day))
inp = sorted(Input(4).read()[:-1].split('\n'))

def parse(line):
    return re.match(r"\[(\d\d\d\d-\d\d-\d\d) (\d\d):(\d\d)] (Guard #(\d+))?(falls asleep)?(wakes up)?", line).groups()

midnight_array = partial(np.zeros, shape=(60))
guards = defaultdict(midnight_array)
for line in inp:
    dt,hr,mn,g,gid,sleeps,wakes = parse(line)
    if g: cur_gid=int(gid)
    if hr=='00' and wakes:  guards[cur_gid][int(mn):] -= 1
    if hr=='00' and sleeps: guards[cur_gid][int(mn):] += 1

# part 1
gid = sorted(guards, key=lambda x: guards[x].sum(), reverse=True)[0]
print(gid * guards[gid].argmax())

# part 2
gid = sorted(guards, key=lambda x: max(guards[x]), reverse=True)[0]
print(gid * guards[gid].argmax())  