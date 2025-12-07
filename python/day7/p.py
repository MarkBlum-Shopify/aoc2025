from functools import cache
from collections import defaultdict, deque


f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


ans = 0
start_row = f[0].strip()
start = (0, 0)
g = defaultdict(lambda: 0)
max_x = 0
max_y = 0
for yi, line in enumerate(f):
    line = line.strip()
    max_y = max(max_y, yi)
    for xi, char in enumerate(line):
        max_x = max(max_x, xi)
        if char == "S":
            start = (xi, yi)
        elif char == "^":
            g[(xi, yi)] = 1

curr = deque([start])
seen = set()
ans = 0
ans_set = set()
while curr:
    curr_node = curr.popleft()
    # print(curr, curr_node, seen)
    # if curr_node in seen:
    #     continue
    next_x = curr_node[0]
    next_y = curr_node[1] + 1
    if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
        if g[(next_x, next_y)] == 1:
            ans += 1
            ans_set.add((next_x, next_y))
            if (
                0 <= next_x + 1 <= max_x
                and 0 <= next_y <= max_y
                and (next_x + 1, next_y) not in seen
            ):
                curr.append((next_x + 1, next_y))
                seen.add((next_x + 1, next_y))
            if (
                0 <= next_x - 1 <= max_x
                and 0 <= next_y <= max_y
                and (next_x + -1, next_y) not in seen
            ):
                curr.append((next_x - 1, next_y))
                seen.add((next_x - 1, next_y))
        else:
            curr.append((next_x, next_y))
            seen.add((next_x, next_y))
print(len(ans_set))  # too high... 1941


# pt 2
ans = 0


@cache
def dfs(curr_node, max_x, max_y):
    # print(curr_node)
    if curr_node[1] == max_y:
        return 1
    if not (0 <= curr_node[0] <= max_x):
        return 1
    if g[curr_node] == 1:
        return dfs((curr_node[0] + 1, curr_node[1] + 1), max_x, max_y) + dfs(
            (curr_node[0] - 1, curr_node[1] + 1), max_x, max_y
        )

    return dfs((curr_node[0], curr_node[1] + 1), max_x, max_y)


ans = dfs(start, max_x, max_y)
print(ans)
