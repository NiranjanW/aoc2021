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


pos, depth = 0, 0
for line in data:
    dpos, ddepth = parse_line(line)
    pos += dpos
    depth += ddepth

ans = pos * depth
print(ans)
