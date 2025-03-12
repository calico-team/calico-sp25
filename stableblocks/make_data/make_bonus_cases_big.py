import random

def make_blocks_for_case():
    num_stacks = 1000

    blocks_lists = [[] for i in range(num_stacks)]

    for j in range(45000):
        k = random.randint(0, num_stacks - 1)
        h = len(blocks_lists[k])
        blocks_lists[k].append(
            (2 * k, 2 + h, 2 * k + 1, 3 + h))

    blocks = sum(blocks_lists, [])

    # Block all stacks are resting on
    blocks.append((0, 1, 2010, 2))
    # Block that block is resting on
    blocks.append((1000, 0, 1100, 1))

    random.shuffle(blocks)

    return blocks

# Num tests
T = 2

print("%d" % T)
for i in range(T):
    blocks = make_blocks_for_case()

    print("%d" % len(blocks))
    for block in blocks:
        print(' '.join('%d' % c for c in block))
