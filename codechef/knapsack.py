
n = 7

profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]



print("PROFITS - ", profits)
print("WEIGHTS - ", weights)

ppw = [[99999999, 1]]

fppw = lambda p, w: round(p / w, 2)

def fppw(p , w) :
    return round(p / w , 2)

for i in range(n):
    x = fppw(profits[i], weights[i])

    for j in range(len(ppw)):
        if x < fppw(ppw[j][0], ppw[j][1]):
            ppw.insert(j, [profits[i], weights[i]])
            break


print(ppw)
ppw = ppw[:-1]
ppw = ppw[::-1]
print("PROFITS PER WEIGHT - ", ppw)

ans = 0
m = 15
for p, w in ppw:
    if m > w:
        ans += p
        m -= w
    else:

        ans += p * m
        break


print(f"TOTAL PROFIT FOR BAG IS {ans}")
