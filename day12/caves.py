from itertools import combinations
from collections import defaultdict

with open("./day12/data1.txt") as fh:
    raw_data = fh.read().strip()
    inp = [i.split("-") for i in raw_data.split("\n")]
    print(inp)

adj = defaultdict(list)

for a,b in inp:
    adj[a].append(b)
    adj[b].append(a)

visited = set()

print(adj)
global ans
ans = 0

def is_small_cave(cave):
    return (cave.islower())

def dfs(cave):

    global ans
    if cave == "end":
        ans +=1
        return
    if is_small_cave(cave) and cave in visited:
        return
    
    if is_small_cave(cave):
        visited.add(cave)
    
    #Add neigbirs to queue

    for nbr in adj[cave]:
        if nbr == "start":
            #Dont visit is again
            continue
        dfs(nbr)
    
    if is_small_cave(cave):
        visited.remove(cave)

dfs("start")


print(ans)