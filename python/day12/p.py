f = open("i.txt").read()


presents = dict()
ans = 0
for region in f.split("\n\n"):
    if "x" in region:
        for i, line in enumerate(region.strip().split("\n")):
            size, needed = line.split(": ")
            needed = [int(x) for x in needed.split()]
            needed = sum([presents[idx][1] * need for idx, need in enumerate(needed)])
            x, y = [int(x) for x in size.split("x")]
            ans += not (needed > (x * y))
    else:
        idx = 0
        present_shape = []
        s = 0
        for i, line in enumerate(region.split("\n")):
            if ":" in line:
                idx = int(line.split(":")[0])
            else:
                present_shape.append([x for x in line.strip()])
                s += sum([1 if x == "#" else 0 for x in line.strip()])
        presents[idx] = (present_shape, s)

print(ans)
