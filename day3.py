
# f = open("raxndom.txt", 'r')


arr = [1, 3, 5, 7]
res = 1

for j in range(4):

    f = open("Tree.txt", 'r')
    shift = arr[j]
    co = 0
    x = -1
    cur = 0
    status = 1
    ch = ''
    for i in f:
        # print(i)

        x += 1
        # print(x)

        if x == 0:
            continue

        # print("hello")
        if '\n' in i:
            i = i[0: len(i) - 1]
        else:
            i = i[0: len(i)]
        # print("ne", len(i))

        # print(i)
        # print(cur, x)

        val = cur + shift
        # print("dfkeoj", val)

        if val < len(i) and val >= 0:
            # print()
            ch = i[val]
            cur = val
            # print(val)

        else:
            # print("sad")

            val = (cur + shift) % len(i)
            cur = val
            ch = i[val]

        # print(x, val)

        if ch == '#':
            # print(x, cur)

            co += 1

    print(arr[j], co)
    res *= co
    # print()


f.close()


print(res*39)
