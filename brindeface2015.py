l = ["FACE"]
count = 0
for n in range(int(input())):
    p = "".join([x for x in input().split()])
    last_w = l[len(l) - 1]
    if last_w[::-1] == p:
        l.pop()
        count += 1
    else:
        l.append(p)
    if len(l) == 0:
        l.append("FACE")
print(count)