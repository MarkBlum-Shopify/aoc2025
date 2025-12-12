f = open("i.txt").read()


grids = dict()
presents = dict()
for region in f.split("\n\n"):
    if "x" in region:
        for i, line in enumerate(region.split("\n")):
            if not line:
                continue
            size, needed = line.split(": ")
            grids[i] = (size, [int(x) for x in needed.split()])
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

    ans = 0
    for k, v in grids.items():
        shape, needed = v
        x, y = [int(x) for x in shape.split("x")]
        total_nums = x * y
        blocks_to_make = 0
        for idx, amnt in enumerate(needed):
            blocks = presents[idx][1]
            blocks_to_make += blocks * amnt
        if blocks_to_make > total_nums:
            continue
        ans += 1

    print(ans)
