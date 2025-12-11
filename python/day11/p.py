from collections import defaultdict
from functools import cache

f = open("i.txt").readlines()


adj = defaultdict(list)


for line in f:
    line = line.strip()
    start, connections = [x.strip() for x in line.split(": ")]
    connections = connections.split()
    adj[start].extend(connections)
print(adj)


@cache
def dfs(node):
    if node == "out":
        return 1
    return sum(dfs(nei) for nei in adj[node])


print(dfs("you"))
# pt 2


@cache
def dfs2(node, seen_fft=False, seen_dac=False):
    seen_fft = seen_fft or node == "fft"
    seen_dac = seen_dac or node == "dac"
    if node == "out":
        if not seen_dac or not seen_fft:
            return 0
        return 1
    return sum(dfs2(nei, seen_fft, seen_dac) for nei in adj[node])


print(dfs2("svr"))
