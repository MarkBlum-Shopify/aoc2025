f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


ranges = []
ids = []
for line in f:
    line = line.strip()
    if "-" in line:
        a, b = [int(x) for x in line.split("-")]
        ranges.append((a, b))
    elif line == "":
        continue
    else:
        ids.append(int(line))

ans = 0
for id in ids:
    for rng in ranges:
        if rng[0] <= id <= rng[1]:
            ans += 1
            break
print(ans)
# 181549686962449001 too high

# pt 2
import heapq

heapq.heapify(ranges)
ans = 0
prev_a, prev_b = heapq.heappop(ranges)
while ranges:
    a, b = heapq.heappop(ranges)
    # print(prev_a, prev_b, a, b, ans)
    # input()
    if a <= prev_b:
        prev_b = max(prev_b, b)
    else:
        ans += prev_b - prev_a + 1
        prev_a = a
        prev_b = b


# print(prev_a, prev_b)
ans += prev_b - prev_a + 1
print(ans)
# 353172468621632 too low
