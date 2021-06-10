f = open("day21.txt", 'r')

co = {}

inr = {}

al = {}


c = 0
for i in f:

    # print("c", c)
    c += 1

    ingred = i[0: i.index('(')-1]

    ing = ingred.split(' ')

    allergen = i[i.index('(') + 10: i.index(')')]
    allergen = allergen.replace(" ", '')

    aller = allergen.split(',')
    # print(aller)
    # print(aller)

    for j in aller:

        if j not in al:
            al[j] = [c]

        else:
            al[j].append(c)

    for j in ing:

        if j not in co:
            inr[j] = [c]
            co[j] = 1

        else:
            inr[j].append(c)
            co[j] += 1


f.close()

# print(al)

# print(co)

# print(al)

# arr = [1, 2, 3]

# a = [1, 2, 3]

# print(set(arr) <= set(a))

# copy_inr = inr.copy()

# copy_co = co.copy()

al = dict(sorted((key, value) for (key, value) in al.items()))

# print(al)
canoc = {}
keyc = 0

for i in al:

    keyc += 1
    canoc[i] = []

    arr = []

    print(i)

    for j in inr:

        if set(al[i]) <= set(inr[j]):

            # if i == "peanuts":
            #     print("p[eanutws")
            # print(set(al[i]))
            # #     print()

            # print(set(inr[j]))

            canoc[i].append(j)

            arr.append(j)

# print(canoc)
res = 0

s = ""

last = {}
print(canoc)


while keyc > 0:
    # print("helo")
    stuff = []
    for i in canoc:

        if len(canoc[i]) == 1:

            stuff.append(i)

            last[i] = canoc[i][0]

            keyc -= 1

            for j in canoc:

                if len(canoc[j]) > 1:

                    if canoc[i][0] in canoc[j] and i != j:
                        canoc[j].remove(canoc[i][0])

    for i in stuff:
        del canoc[i]


# print(last)
last = dict(sorted((key, value) for (key, value) in last.items()))

s = ''


for i in last:
    print(i)
    s += last[i]
    s += ','

print(s[0:-1])
# [1, 4, 8, 10, 23, 30, 33, 35, 39]
