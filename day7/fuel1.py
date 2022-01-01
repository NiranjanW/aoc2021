with open("./day7/data.txt") as fin:
    raw_data = fin.read().strip().split(",")

data = [int(i) for i in raw_data]
data.sort()
ans = 1 << 60


def C2(d):
    return d * (d + 1) / 2


for med in range(len(data)):
    score = 0
    for x in data:
        d = abs(x - med)
        score += C2(d)
    if score < ans:
        ans = score
print(ans)
