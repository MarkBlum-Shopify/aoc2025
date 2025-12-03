import heapq

f = open("i.txt").readlines()

ans = 0

for line in f:
    line = line.strip()
    m = 0
    for ai, a in enumerate(line):
        for b in line[ai + 1 :]:
            m = max(m, int(a + b))
    ans += m


print(ans)

# pt 2
# f = ["234234234234278"]
total = 0
for line in f:
    line = line.strip()
    ans = []
    while len(ans) != 12:
        prev_end_idx = ans[-1][1] if ans else -1
        candidate = (0, -1)
        # print(prev_end_idx + 1, len(line) - (12 - len(ans)) + 1, ans)
        for i in range(prev_end_idx + 1, len(line) - (12 - len(ans)) + 1):
            if int(line[i]) > candidate[0]:
                candidate = (int(line[i]), i)
        ans.append(candidate)
    # print(line)
    # print(ans)
    t = int("".join([str(x[0]) for x in ans]))
    total += t

print(total)
# min_heap = []
# for num in line:
#     print(num, min_heap)
#     if len(min_heap) == 12:
#         if min_heap[0] < int(num):
#             min_heap.pop()
#             min_heap.append(int(num))
#             # heapq.heappop(min_heap)
#             # heapq.heappush(min_heap, int(num))
#     else:
#         min_heap.append(int(num))
#         # heapq.heappush(min_heap, int(num))
# m = int("".join([str(x) for x in min_heap]))
# print(m)
# ans += m


# print(ans)
# 74478153522085 too low...
exit()
f = ["811111111111119"]
ans = 0
for line in f:
    line = line.strip()
    m = 0
    for ai, a in enumerate(line):
        for bi, b in enumerate(line[ai + 1 :]):  # 1
            for ci, c in enumerate(line[bi + 1 :]):  # 2
                for di, d in enumerate(line[ci + 1 :]):  # 3
                    for ei, e in enumerate(line[di + 1 :]):  # 4
                        for fi, f in enumerate(line[ei + 1 :]):  # 5
                            for ii, i in enumerate(line[fi + 1 :]):  # 6
                                for ji, j in enumerate(line[ii + 1 :]):  # 7
                                    for ki, k in enumerate(line[ji + 1 :]):  # 8
                                        for li, l in enumerate(line[ki + 1 :]):  # 9
                                            for ni, n in enumerate(
                                                line[li + 1 :]
                                            ):  # 10
                                                for oi, o in enumerate(
                                                    line[ni + 1 :]
                                                ):  # 11
                                                    m = max(
                                                        m,
                                                        int(
                                                            a
                                                            + b
                                                            + c
                                                            + d
                                                            + e
                                                            + f
                                                            + i
                                                            + j
                                                            + k
                                                            + l
                                                            + n
                                                            + o
                                                        ),
                                                    )
    ans += m


print(ans)
