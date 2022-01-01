
with open("./day9/data1.txt") as inp:
    raw_data = inp.read().strip().split("\n")
    map = [[int(i) for i in list(line)]for line in raw_data]
print(map)

rows = len(map)
columns = len(map[0])

print(rows, columns)
for row in range(rows):
    for col in range(columns):
        low = True
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = row + d[0]
            cc = col + d[1]
    print(rr, cc)
