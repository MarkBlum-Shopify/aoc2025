from collections import defaultdict
import heapq
import math

z = 1000
f = open("i.txt").readlines()
# f = open("ii.txt").readlines()
# z = 10


node_to_component = dict()

component_to_node = defaultdict(set)


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


h = []

for i in range(len(f)):
    a = tuple((int(x) for x in f[i].strip().split(",")))
    for j in range(i + 1, len(f)):
        b = tuple((int(x) for x in f[j].strip().split(",")))
        heapq.heappush(h, (dist(a, b), a, b))

num_of_circuts = len(h)
# print(len(h))

curr_component = 0

for _ in range(z):
    length, a, b = heapq.heappop(h)
    # print(length, a, b)
    # print(node_to_component)
    # print(component_to_node)
    if a not in node_to_component and b not in node_to_component:
        node_to_component[a] = curr_component
        node_to_component[b] = curr_component
        component_to_node[curr_component].add(a)
        component_to_node[curr_component].add(b)
        curr_component += 1
    elif a in node_to_component and b not in node_to_component:
        node_to_component[b] = node_to_component[a]
        component_to_node[node_to_component[a]].add(b)
    elif b in node_to_component and a not in node_to_component:
        node_to_component[a] = node_to_component[b]
        component_to_node[node_to_component[b]].add(a)
    elif a in node_to_component and b in node_to_component:
        # move all b to a
        if node_to_component[a] == node_to_component[b]:
            continue
        to_delete = node_to_component[b]
        for to_move in component_to_node[node_to_component[b]]:
            component_to_node[node_to_component[a]].add(to_move)
            node_to_component[to_move] = node_to_component[a]
        del component_to_node[to_delete]
    else:
        print("what??")
    # print("after")
    # print(node_to_component)
    # print(component_to_node)
    # input()

biggest = sorted([len(v) for v in component_to_node.values()])[::-1][:3]
ans = 1
for e in biggest:
    ans *= e
print(ans)

node_to_component = dict()

component_to_node = defaultdict(set)


h = []

for i in range(len(f)):
    a = tuple((int(x) for x in f[i].strip().split(",")))
    for j in range(i + 1, len(f)):
        b = tuple((int(x) for x in f[j].strip().split(",")))
        heapq.heappush(h, (dist(a, b), a, b))

num_of_circuts = len(f)

curr_component = 0
while h:
    length, a, b = heapq.heappop(h)
    # print(length, a, b)
    # print(node_to_component)
    # print(component_to_node)
    if a not in node_to_component and b not in node_to_component:
        node_to_component[a] = curr_component
        node_to_component[b] = curr_component
        component_to_node[curr_component].add(a)
        component_to_node[curr_component].add(b)
        curr_component += 1
    elif a in node_to_component and b not in node_to_component:
        node_to_component[b] = node_to_component[a]
        component_to_node[node_to_component[a]].add(b)
        if len(component_to_node[node_to_component[a]]) == num_of_circuts:
            print(a[0] * b[0])
            exit()
    elif b in node_to_component and a not in node_to_component:
        node_to_component[a] = node_to_component[b]
        component_to_node[node_to_component[b]].add(a)
        if len(component_to_node[node_to_component[a]]) == num_of_circuts:
            print(a[0] * b[0])
            exit()
    elif a in node_to_component and b in node_to_component:
        # move all b to a
        if node_to_component[a] == node_to_component[b]:
            continue
        to_delete = node_to_component[b]
        for to_move in component_to_node[node_to_component[b]]:
            component_to_node[node_to_component[a]].add(to_move)
            node_to_component[to_move] = node_to_component[a]
        if len(component_to_node[node_to_component[a]]) == num_of_circuts:
            print(a[0] * b[0])
            exit()
        del component_to_node[to_delete]
    else:
        print("what??")
