f = open("Tree.txt", 'r')

# 127272600
co = 0
cur = 0
x = -1

for i in f:
    i = i[0: len(i) - 1]

    x += 1

    if x == 0 or x % 2 != 0:
        continue

    # print("hello")
    # i = i[0: len(i) - 1]

    # print(i)

    val = cur + 1
    # print(val)

    if val < len(i) and val >= 0:
        ch = i[val]
        cur = val
        # print(val)

    else:

        val = 0
        cur = val
        ch = i[val]

    if ch == '#':
        print(str(x + 1) + " " + str(val + 1))

        co += 1


f.close()
print(co)

print(39 * 43531330500)
