with open("./day2/data.txt") as inp:
    data = [line for line in inp.read().strip().split("\n")]


def parse_line(line):
    position, value = line.split(" ")
    value = int(value)
    if position == "forward":
        return (value, 0)
    elif position == "down":
        return (0, value)
    else:
        return (0, -value)


def parse_line(line, prev_aim):
    position, value = line.split(" ")
    value = int(value)

    if position == "forward":
        return (value, value * prev_aim, 0)
    elif position == "down":
        return (0, 0, value)
    else:
        return (0, 0, -value)


pos, depth, aim = 0, 0, 0
for line in data:
    dpos, ddepth, daim = parse_line(line, aim)
    pos += dpos
    depth += ddepth
    aim += daim

ans = pos * depth
print(ans)
