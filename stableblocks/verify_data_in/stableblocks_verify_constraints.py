import re

pos_int_re = re.compile(r'^[1-9]\d*$')
int_pattern = r'(0|-?[1-9]\d*)'
block_re = re.compile(r'^' + ' '.join(4 * [int_pattern]) + '$')

if __name__ == '__main__':
    import sys

    lines = open(sys.argv[1]).read().split('\n')

    line_no = 0

    total_mass = 0

    m = pos_int_re.match(lines[line_no])
    if not m:
        raise Exception("Bad line %d" % line_no)
    line_no += 1
    T = int(m.group(0))

    for i in range(T):
        m = pos_int_re.match(lines[line_no])
        if not m:
            raise Exception("Bad line %d" % line_no)
        line_no += 1
        N = int(m.group(0))

        for j in range(N):
            m = block_re.match(lines[line_no])
            if not m:
                raise Exception("Bad line %s %d" % (lines[line_no], line_no))
            line_no += 1
            x0, y0, x1, y1 = [int(s) for s in m.groups()]
            if not x1 > x0:
                raise Exception("Not x1 > x0")
            if not y1 > y0:
                raise Exception("Not x1 > x0")
            if not y0 >= 0:
                raise Exception("Not y0 >= 0")
            if not x0 > -10000:
                raise Exception("Not x0 > -10000")
            if not x0 < 10000:
                raise Exception("Not x0 < 10000")
            total_mass += (x1 - x0) * (y1 - y0)

    if not total_mass < 100000:
        raise Exception("Not total_mass = %d < 100000" % total_mass)

    if lines[line_no] != '':
        raise Exception("Not ending with new line")
    line_no += 1

    if line_no != len(lines):
        raise Exception("Wrong number lines %d %d" % (line_no, len(lines)))
