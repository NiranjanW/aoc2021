with open("./day11/data.txt") as inp:
    raw_data = inp.read().split()
G = []
for line in raw_data:
    G.append([int(x) for x in line.strip()])

R = len(G)
C = len(G[0])

# print(G, R, C)


def flash(r, c):
    ans = 0
    ans += 1

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != -1:
                print(rr, cc)


for r in range(R):
    for c in range(C):
        flash(r, c)
