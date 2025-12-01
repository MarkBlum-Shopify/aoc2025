lines = open("i.txt").readlines()

pos = 50
ans = 0
# 6029 too low

for line in lines:
    direction = line[0]
    to_turn = int(line[1:].strip())
    if direction == "L":
        for i in range(to_turn):
            pos = (pos - 1) % 100
            if pos == 0:
                ans += 1
    elif direction == "R":
        for i in range(to_turn):
            pos = (pos + 1) % 100
            if pos == 0:
                ans += 1
print(ans)
