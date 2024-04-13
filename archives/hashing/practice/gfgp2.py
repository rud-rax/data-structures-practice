arr = "10 20 30 40 10"
arr = list(map(int, arr.rstrip().split()))
print(arr)

d1 = {}

for ele in arr:
    if ele in d1.keys():
        d1[ele] += 1

    else:
        d1[ele] = 1

# print(d1)

c = []
for k in d1.keys():
    if d1[k] == 1:
        c.append(k)

print(f"ANS -> {c[0]}")
