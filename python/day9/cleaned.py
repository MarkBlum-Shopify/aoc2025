from functools import cache

f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


ans = 0

points = []
for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    points.append((ax, ay))
    for j in range(i + 1, len(f)):
        bx, by = [int(x) for x in f[j].strip().split(",")]
        width = abs(bx - ax) + 1
        length = abs(by - ay) + 1
        ans = max(ans, width * length)
print(ans)
p1 = ans
# 1 == red, 2 == green
g = dict()

ans = 0


previous = None
start = [int(x) for x in f[0].strip().split(",")]
for i in range(len(f)):
    ax, ay = [int(x) for x in f[i].strip().split(",")]
    g[(ax, ay)] = 1
    if previous:
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
for greenyi in range(min(start[1], previous[1]), max(previous[1], start[1]) + 1):
    for greenxi in range(min(start[0], previous[0]), max(previous[0], start[0]) + 1):
        if (greenxi, greenyi) in g:
            continue
        else:
            g[(greenxi, greenyi)] = 2

edges = []

for i in range(len(points)):
    p1, p2 = points[i], points[(i + 1) % len(points)]
    edges.append((min(p1[1], p2[1]), max(p1[1], p2[1]), max(p1[0], p2[0])))


@cache
def even_odd_test(point):
    if point in g:
        return True
    count = 0
    cx, cy = point

    for y1, y2, x2 in edges:
        if y1 < cy <= y2:
            if cx < x2:
                count += 1

    return count % 2


ans = 0

for i in range(len(points)):
    ax, ay = points[i]
    for j in range(i + 1, len(points)):
        bx, by = points[j]
        fail = False
        width = abs(bx - ax) + 1
        length = abs(by - ay) + 1
        t = width * length
        if t <= ans:
            continue

        corners = [(ax, ay), (ax, by), (bx, ay), (bx, by)]
        if not all(even_odd_test(c) for c in corners):
            continue

        for py in range(min(ay, by), max(ay, by) + 1):
            if not even_odd_test((ax, py)):
                fail = True
                break
            if not even_odd_test((bx, py)):
                fail = True
                break
        if fail:
            continue

        for px in range(min(ax, bx), max(ax, bx) + 1):
            if not even_odd_test((px, ay)):
                fail = True
                break
            if not even_odd_test((px, by)):
                fail = True
                break
        if fail:
            continue

        if t > ans:
            ans = t
            print("New ans: ", ans)
        ans = max(ans, width * length)
print(ans)
