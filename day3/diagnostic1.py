with open("./day3/data1.txt") as inp:
    data = [i for i in inp.read().strip().split()]

N = len(data[0])
data = [int(i, 2) for i in data]
# print(data)
o2_rem = data.copy()
# print(o2_rem)
pos = N - 1

# while pos >= 0 and len(o2_rem) > 1:
#     pass
#     # Find most common bit
# ones = sum[((x & (1 << pos)) >> pos) for x in o2_rem]


if __name__ == "__main__":
    while pos >= 0 and len(o2_rem) > 1:
        # Find most common bit
        ones = sum([((x & (1 << pos)) >> pos) for x in o2_rem])
        zeros = len(o2_rem) - ones

        if zeros > ones:
            o2_rem = list(filter(lambda x: not (x & (1 << pos)) >> pos))
        else:
            o2_rem = list(filter(lambda x: (x & (1 << pos)) >> pos))
    pos -= 1
