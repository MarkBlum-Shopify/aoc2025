from collections import deque
from functools import cache

f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


ans = 0
min_x = 1e99
min_y = 1e99
max_x = 0
max_y = 0


points = []
combos = []
for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    points.append((ax, ay))
    for j in range(i + 1, len(f)):
        bx, by = [int(x) for x in f[j].strip().split(",")]
        combos.append([(ax, ay), (bx, by)])
        width = abs(bx - ax) + 1
        length = abs(by - ay) + 1
        min_x = min(min_x, ax, bx)
        min_y = min(min_y, ay, by)
        max_x = max(max_x, ax, bx)
        max_y = max(max_y, ay, by)
        ans = max(ans, width * length)
print(ans)
p1 = ans
# 1 == red, 2 == green
g = dict()

ans = 0

greens = []

previous = None
start = [int(x) for x in f[0].strip().split(",")]
for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    g[(ax, ay)] = 1
    if previous:
        greens.append([(ax, ay), (previous[0], previous[1])])
        for greenyi in range(min(ay, previous[1]), max(previous[1], ay) + 1):
            for greenxi in range(min(ax, previous[0]), max(previous[0], ax) + 1):
                if (greenxi, greenyi) in g:
                    continue
                else:
                    g[(greenxi, greenyi)] = 2
    previous = (
        ax,
        ay,
    )
greens.append([(start[0], start[1]), (previous[0], previous[1])])
for greenyi in range(min(start[1], previous[1]), max(previous[1], start[1]) + 1):
    for greenxi in range(min(start[0], previous[0]), max(previous[0], start[0]) + 1):
        if (greenxi, greenyi) in g:
            continue
        else:
            g[(greenxi, greenyi)] = 2


@cache
def even_odd_test(point):
    if point in g:
        return True
    count = 0
    cx, cy = point
    # print(new)

    p1 = points[0]
    for i in range(len(points) + 1):
        p2 = points[i % len(points)]
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        x2 = max(p1[0], p2[0])
        if y1 < cy <= y2:
            if cx < x2:
                count += 1
        p1 = p2

    return count % 2


# NOT MY SOLUTION, taken from /u/Friiits to understand a better way

sort = lambda l: [
    ((min(a, c), min(b, d)), (max(a, c), max(b, d))) for (a, b), (c, d) in l
]
# print(sort(greens))
# input()
s_greens = sort(greens)

ans = 0
for (x, y), (u, v) in combos:
    x1 = min(x, u)
    y1 = min(y, v)
    x2 = max(x, u)
    y2 = max(y, v)
    t = (x2 - x1 + 1) * (y2 - y1 + 1)
    if t > ans:
        for (p, q), (r, s) in s_greens:
            gx1 = p
            gx2 = r
            gy1 = q
            gy2 = s
            # gx1 = min(p, r)
            # gy1 = min(q, s)
            # gx2 = max(p, r)
            # gy2 = max(q, s)

            if gx1 < x2 and gy1 < y2 and gx2 > x1 and gy2 > y1:
                break
        else:
            ans = t
print(ans)


ans = 0

for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    for j in range(i + 1, len(f)):
        bx, by = [int(x) for x in f[j].strip().split(",")]
        fail = False
        for py in range(min(ay, by), max(ay, by) + 1):
            width = abs(bx - ax) + 1
            length = abs(by - ay) + 1
            t = width * length
            if t <= ans or t >= p1:
                continue
            # print(ax, ay, bx, by, (ax, py), even_odd_test((ax, py), points, g))
            if not even_odd_test((ax, py)):
                fail = True
            if fail:
                break
            if not even_odd_test((bx, py)):
                fail = True
            if fail:
                break

        for px in range(min(ax, bx), max(ax, bx) + 1):
            # print(ax, ay, bx, by, (px, ay), even_odd_test((px, ay), points, g))
            if not even_odd_test((px, ay)):
                fail = True
            if fail:
                break
            if not even_odd_test((px, by)):
                fail = True
            if fail:
                break
        if fail:
            continue

        width = abs(bx - ax) + 1
        length = abs(by - ay) + 1
        t = width * length
        if t > ans:
            ans = t
            print("New ans: ", ans)
        ans = max(ans, width * length)
print(ans)
exit()
min_x = 1e99
min_y = 1e99
max_x = 0
max_y = 0
# q = deque([(previous[0] + 1, previous[1] + 1)])
# directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


#
# print("Starting bfs")
# while q:
#     cx, cy = q.popleft()
#     if cx < 0 or cy < 0:
#         print("OHHH NOOOO: ", cx, cy)
#     for dx, dy in directions:
#         px = cx + dx
#         py = cy + dy
#         if (px, py) in g:
#             continue
#         else:
#             g[(px, py)] = 2
#             q.append((px, py))
#

print("Done with bfs")
# print(len(g))
ans = 0
for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    for j in range(i + 1, len(f)):
        bx, by = [int(x) for x in f[j].strip().split(",")]
        fail = False
        for y in range(min(ay, by), max(ay, by) + 1):
            for x in range(min(ax, bx), max(ax, bx) + 1):
                if (x, y) not in g:
                    fail = True
                if fail:
                    break
            if fail:
                break
        if fail:
            continue

        width = abs(bx - ax) + 1
        length = abs(by - ay) + 1
        # print(width * length, (ax, ay), (bx, by))
        t = width * length
        if t > ans:
            ans = t
            print("New ans: ", ans)
# print(min_x, max_y, min_y, max_y)
print(ans)
exit()
for iy in range(min_y, max_y + 1):
    row = []
    for ix in range(min_x, max_x + 1):
        if (ix, iy) not in g:
            row.append(".")
        elif g[(ix, iy)] == 1:
            row.append("#")
        else:
            row.append("O")
    print("".join(row))

print(ans)
