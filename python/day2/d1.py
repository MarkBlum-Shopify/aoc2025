f = open("i.txt").readlines()[0]

ans = 0

ranges = [x.strip() for x in f.split(",")]

# ranges = ["95-115"]
for rng in ranges:
    a, b = [int(x) for x in rng.split("-")]
    for num in range(a, b + 1):
        if num > 10:
            s_num = str(num)
            if len(s_num) % 2 == 0:
                if s_num[: len(s_num) // 2] == s_num[len(s_num) // 2 :]:
                    ans += num

print(ans)
# 49339815033 too high
ans = 0
for rng in ranges:
    a, b = [int(x) for x in rng.split("-")]
    for num in range(a, b + 1):
        if num > 10:
            s_num = str(num)
            digits = len(s_num)
            prefix = ""
            for chr in s_num:
                prefix += chr
                if s_num.count(prefix) * len(prefix) == digits and prefix != s_num:
                    # print(num, prefix)
                    ans += num
                    break

print(ans)
# 2057620109604641 too high
# 2057578814624800 too high
