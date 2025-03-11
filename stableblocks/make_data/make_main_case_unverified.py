import sys
import random

x_size = 200
x_dither = 1
y_dither = 40
num_levels = 4

shift = 0.5
probability = 0.0

def add_layer(blocks):
    new_blocks = []
    
    for x0, y0, x1, y1 in blocks:
        l = [x0 + random.randint(-x_dither,x_dither), y1, x0 + (x1 - x0) // 3 + random.randint(x_dither,x_dither), y1 + random.randint(1,y_dither)]
        r = [x0 + 2 * (x1 - x0) // 3 + random.randint(-x_dither,x_dither), y1, x1 + random.randint(-x_dither,x_dither), y1 + random.randint(1,y_dither)]

        if random.random() < probability:
            s = int((l[2] - l[0]) * shift)
            l[0] -= s
            l[2] -= s
        if random.random() < probability:
            s = int((r[2] - r[0]) * shift)
            r[0] += s
            r[2] += s

        if not l[0] < l[2]:
            raise Exception()
        if not l[2] < r[0]:
            raise Exception()
        if not r[0] < r[2]:
            raise Exception()

        new_blocks.append(l)
        new_blocks.append(r)

    return new_blocks

blocks = [(-x_size, 0, x_size, 10)]
all_blocks = blocks
for i in range(num_levels):
    blocks = add_layer(blocks)
    all_blocks += blocks

print(len(all_blocks))
for x0, y0, x1, y1 in all_blocks:
    print(x0, y0, x1, y1)

      
