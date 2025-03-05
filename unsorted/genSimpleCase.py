import sys

import random

max_size = 25

blocks = []

def simple(s, n, stable):

    global blocks
    
    x0 = s * max_size + random.randint(5,8)
    x1 = x0 + random.randint(1,3)

    y0 = 0
    y1 = random.randint(3,10)

    blocks.append((x0,y0,x1,y1))

    for i in range(n):
        y0, y1 = y1, y1 + random.randint(2,5)

        w = random.randint(1,2)
        blocks.append((x0 - w, y0, x1 + w, y1))

    if not stable:
        y0, y1 = y1, y1 + random.randint(2,5)
        blocks.append((x0, y0, x1 + 10, y1))

    y0, y1 = y1, y1 + random.randint(2,5)

    w = random.randint(1,2)
    blocks.append((x0 - w, y0, x1 + w, y1))

for i in range(100):
    simple(i, random.randint(2,100), i != 16)

print(len(blocks))

random.shuffle(blocks)

for block in blocks:
    for c in block:
        print(c, end=' ')
    print()




    
