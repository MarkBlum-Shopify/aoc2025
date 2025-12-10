import math
from collections import deque
import heapq

f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


def flip(curr, wiring):
    l = list(curr)
    for el in wiring:
        if l[el] == ".":
            l[el] = "#"
        else:
            l[el] = "."
    return l


ans = 0
for line in f:
    line = line.strip()
    target, *wirings, joltage = line.split()
    wirings = [set([int(x) for x in w[1:-1].split(",")]) for w in wirings]
    target = list(target[1:-1])
    base_start = ["." for _ in target]
    # steps, curr_target
    q = deque([(0, base_start)])
    found = False
    while q:
        steps, curr_target = q.popleft()
        for wire in wirings:
            flipped = flip(curr_target, wire)
            if flipped == target:
                ans += steps + 1
                found = True
                break
            q.append((steps + 1, flipped))
        if found:
            break

print(ans)


# heuristic is how "close" we are to the target joltage
def h(joltage_target, curr_joltage):
    return max(a - b for a, b in zip(joltage_target, curr_joltage))
    # ans = 0
    #
    # for a, b in zip(joltage_target, curr_joltage):
    #     ans += (a - b) ** 2
    # return math.sqrt(ans)


def is_over(joltage_target, curr_joltage):
    for a, b in zip(joltage_target, curr_joltage):
        if b > a:
            return True
    return False


def increment(curr_joltage, wire):
    j = list(curr_joltage)
    for el in wire:
        j[el] += 1
    return tuple(j)


from z3 import *


def generate_vector(wiring, joltage_target):
    t = [0 for _ in joltage_target]
    for el in wiring:
        t[el] = 1
    return t


ans = 0
for line in f:
    line = line.strip()
    target, *wirings, joltage = line.split()
    joltage_target = tuple([int(x) for x in joltage[1:-1].split(",")])
    wirings = [set([int(x) for x in w[1:-1].split(",")]) for w in wirings]
    ints = {
        Int(str(i)): generate_vector(wirings[i], joltage_target)
        for i in range(len(wirings))
    }
    o = Optimize()
    for k, v in ints.items():
        o.add(k >= 0)
    for i in range(len(joltage_target)):
        o.add(sum(k * v[i] for k, v in ints.items()) == joltage_target[i])
    o.minimize(sum(k for k in ints.keys()))
    o.check()
    # print(line)
    # print(o.model())
    modeled = o.model()
    # print(sum([modeled[x].as_long() for x in modeled]))
    ans += sum([modeled[x].as_long() for x in modeled])
    continue
    # 20372 too high........

    base_joltage = tuple([0 for _ in joltage_target])
    # steps, heuristic, joltage
    heap = []
    print(joltage_target, base_joltage, h(joltage_target, base_joltage))
    heapq.heappush(heap, (0 + h(joltage_target, base_joltage), 0, base_joltage))
    # heapq.heappush(heap, (h(joltage_target, base_joltage), 0, base_joltage))
    found = False
    seen = set()
    while heap:
        heuristic, steps, curr_joltage = heapq.heappop(heap)
        # heuristic, steps, curr_joltage = heapq.heappop(heap)
        # print(steps, heuristic, curr_joltage)
        # input()
        if curr_joltage in seen:
            continue
        if curr_joltage == joltage_target:
            ans += steps
            print(ans)
            found = True
            break
        seen.add(curr_joltage)
        for wire in wirings:
            incremented = increment(curr_joltage, wire)
            if is_over(joltage_target, incremented):
                continue
            if incremented in seen:
                continue
            # if incremented == joltage_target:
            #     ans += steps + 1
            #     print(ans)
            #     found = True
            #     break
            heapq.heappush(
                heap,
                (steps + 1 + h(joltage_target, incremented), steps + 1, incremented),
            )
        if found:
            break

print(ans)
