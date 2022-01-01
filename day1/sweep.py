with open("./day1/data.txt") as inp:
    data = [int(i) for i in inp.read().strip().split("\n")]

N = len(data)

# count = 0
# for i in range(1, N):
#     if data[i] > data[i - 1]:
#         count += 1
# print(count)


# Compute moving avg
count1 = 0
prev_mov_sum = 1 << 60
moving_sum = sum(data[:5])

for i in range(N - 5):

    if moving_sum > prev_mov_sum:
        count1 += 1
    prev_mov_sum = moving_sum
    # update moving sum
    moving_sum -= data[i]
    prev_mov_sum += data[i + 5]

#     print(moving_sum, prev_mov_sum)
# print(count1)

if moving_sum > prev_mov_sum:
    print += 1
