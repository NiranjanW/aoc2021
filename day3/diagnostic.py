with open("./day3/data.txt") as inp:
    data = [i for i in inp.read().strip().split()]


# for i in data:
#     print(data)
N = len(data[0])

# def digit(line: str) -> int:
#     max = ""
#     for j in line:
#         print(j[:1])

gamma_rate = [None] * N
epsilon_rate = [None] * N

for i in range(N):
    zeros = sum([data[j][i] == "0" for j in range(len(data))])
    ones = sum([data[j][i] == "1" for j in range(len(data))])
    if zeros > ones:
        gamma_rate[i] = "0"
        epsilon_rate[i] = "1"
    else:
        gamma_rate[i] = "1"
        epsilon_rate[i] = "0"

ans = int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)
print(gamma_rate, epsilon_rate)
print(ans)
