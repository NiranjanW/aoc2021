
with open("./day8/data1.txt") as inp:
    raw_data = inp.read().strip().split("\n")
    second_part = [line[line.index("|")+2:].strip(" ") for line in raw_data]
print(second_part)
