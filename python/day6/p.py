from functools import reduce

f = open("i.txt").readlines()
# f = open("ii.txt").readlines()


operators = [x.strip() for x in f[-1].strip().split()]
numbers = [1 if x == "*" else 0 for x in operators]

for line in f[:-1]:
    for idx, number in enumerate(line.split()):
        if operators[idx] == "+":
            numbers[idx] += int(number)
        else:
            numbers[idx] *= int(number)

print(sum(numbers))
# 3525371264400 too high

operators = [x.strip() for x in f[-1].strip().split()]
numbers = []

ans = 0
row_numbers = []
curr_num = ""
last_operator = ""
for idx in range(len(f[0])):
    if f[0][idx] == "\n":
        continue
    if row_numbers and f[-1][idx] in ["+", "*"]:
        if last_operator == "+":
            ans += sum(row_numbers)
        if last_operator == "*":
            ans += reduce(lambda x, y: x * y, row_numbers, 1)
        row_numbers = []
        curr_num = ""
    if f[-1][idx] in ["+", "*"]:
        last_operator = f[-1][idx]
    for row in f[:-1]:
        curr_num += row[idx]
    # print(idx, curr_num, row_numbers, ans)
    if curr_num.strip():
        row_numbers.append(int(curr_num.strip()))
        curr_num = ""

if last_operator == "+":
    ans += sum(row_numbers)
if last_operator == "*":
    ans += reduce(lambda x, y: x * y, row_numbers, 1)
print(ans)
exit()

# for line in f:
#     for idx in range(len(line)):

for line in f[:-1]:
    row = []
    for idx, number in enumerate(line.split()):
        row.append(number)
        # if operators[idx] == "+":
        #     numbers[idx] += int(number)
        # else:
        #     numbers[idx] *= int(number)
    numbers.append(row)

ans = 0
for col in range(len(numbers[0])):
    col_nums = []
    for row in range(len(numbers)):
        col_nums.append(numbers[row][col])
    longest = max([len(x) for x in col_nums])
    col_nums = [x.rjust(longest, "x") for x in col_nums]
    n = []
    for idx in range(longest):
        s = ""
        for num in col_nums:
            s += num[idx]
        n.append(int(s.lstrip("x").rstrip("x")))
    if operators[col] == "+":
        print(n, sum(n))
        ans += sum(n)
    if operators[col] == "*":
        print(n, reduce(lambda x, y: x * y, n, 1))
        ans += reduce(lambda x, y: x * y, n, 1)


print(ans)
# print(sum(numbers))
