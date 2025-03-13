import sys
import random

def add_layer(blocks, probability, shift, x_dither, y_dither):
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

def make_test(x_size, x_dither, y_dither, num_levels, shift, probability, l = 10):
    blocks = [(-x_size, 0, x_size, l)]
    all_blocks = blocks
    for i in range(num_levels):
        blocks = add_layer(blocks, probability, shift, x_dither, y_dither)
        all_blocks += blocks

    print(len(all_blocks))
    for block in all_blocks:
        print(' '.join('%d' % c for c in block))

random.seed(423426345)
        
print("9")
make_test(200, 1, 40, 4, 0.5, 0.5)
make_test(400, 1, 10, 5, 0.5, 0.01, 12)
make_test(100, 1, 40, 3, 0.15, 0.01)
make_test(1800, 1, 2, 6, 0.2, 0.04, 1)
make_test(1700, 1, 2, 6, 0.3, 0.04, 1)
make_test(100, 1, 10, 3, 0.15, 0.01)
make_test(100, 1, 10, 3, 0.15, 0.01)
make_test(100, 1, 10, 3, 0.15, 0.01)
make_test(400, 1, 10, 5, 0.5, 0.03, 12)

