piles = [9,8,7,6,5,1,2,3,4]
x = 0
y = 0
z = 0


while piles != []:
    w = 0
    for i in range(len(piles)):
        if w < piles[i]:
            w = piles[i]
            k = i
    x += w
    del piles[k]

    w = 0
    for i in range(len(piles)):
        if w < piles[i]:
            w = piles[i]
            k = i
    y += w
    del piles[k]

    w = x
    for i in range(len(piles)):
        if w > piles[i]:
            w = piles[i]
            k = i
    z += w
    del piles[k]

print(y)
