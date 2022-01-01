# with open("./day7/data1.txt") as inp:
#     data = [int(i) for i in inp.read().strip().split(",")]
# # print(data)
# ans = 1 << 10

# max_pos = max(data)
# # end_pos = data[1]
# for pos in range(max_pos):
#     req = 0
#     for i in data:
#         req += abs(pos - req)
#     ans = min(ans, req)
# print(ans)


with open("./day7/data.txt") as fin:
    raw_data = fin.read().strip().split(",")

data = [int(i) for i in raw_data]

data.sort()
ans = 1 << 60


for med in range(len(data)):
    score = 0
    for x in data:
        d = abs(x - med)
        score += d
    ans = min(ans, score)
#     result.append(score)
# ans = min(result)
print(ans)
# ans = 1 << 60

# max_pos = max(data)

# for pos in range(max_pos):
#     req = 0
#     for i in data:
#         req += abs(i - req)
#         print(req)
#     ans = min(ans, req)

# print(ans)
