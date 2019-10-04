import fileinput

t = [1]
print(t)
for i in range(1, 101):
    t.append(t[i - 1]*i)

for r in fileinput.input():
    r = r[:-1]
    comb = t[len(r)]
    c = [0] * 128
    for s in r:
        c[ord(s)] += 1
    for i in c:
        if i > 0:
            comb //= t[i]
    print(comb)
