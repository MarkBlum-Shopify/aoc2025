from collections import defaultdict

f = open("i.txt").readlines()


g = dict()


for yi, line in enumerate(f):
    line = line.strip()
    for xi, char in enumerate(line):
        if char == ".":
            pass
            # g[(yi, xi)] = 0
        else:
            g[(yi, xi)] = 1
ans = 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
for k, v in g.items():
    c = 0
    py = k[0]
    px = k[1]
    for dy, dx in directions:
        if (py + dy, px + dx) in g:
            c += 1
    if c < 4:
        ans += 1

print(ans)


ans = 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
while True:
    g_keys = list(g.keys())
    prev_ans = ans
    for k in g_keys:
        c = 0
        py = k[0]
        px = k[1]
        for dy, dx in directions:
            if (py + dy, px + dx) in g:
                c += 1
        if c < 4:
            del g[(py, px)]
            ans += 1
    if prev_ans == ans:
        break

print(ans)
# 3446 too low
