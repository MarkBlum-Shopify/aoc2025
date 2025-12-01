lines = open("i.txt").readlines()

pos = 50
ans = 0

for line in lines:
    direction = line[0]
    to_turn = int(line[1:].strip())
    if direction == "L":
        pos = (pos - to_turn) % 100
    elif direction == "R":
        pos = (pos + to_turn) % 100
    if pos == 0:
        ans += 1

print(ans)
