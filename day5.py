f = open("day5.txt", 'r')

maxid = -1


arr = []
for i in f:

    st = 0
    en = 127

    i = i[0:len(i) - 1]
    row = 0
    ch = ""
    print(i)

    for j in range(0, len(i) - 3):
        print(i[j], end="")
        # mid = (st + en) // 2
        if i[j] == "F":
            en = (st + en) // 2
            ch = "F"
        elif i[j] == "B":
            st = ((st+en) // 2) + 1
            ch = "B"

        print(st, en)

    if ch == "F":
        row = st
    else:
        row = en
    print()

    st = 0
    col = 0
    en = 7
    for j in range(len(i) - 3, len(i)):
        print(i[j], end="")
        if i[j] == 'L':
            en = (st + en) // 2
            ch = "L"

        elif i[j] == 'R':
            st = ((st + en) // 2) + 1
            ch = "R"

    if ch == "L":
        col = st
    else:
        col = en

    arr.append((row * 8)+col)

    maxid = max(maxid, (row * 8)+col)
    print()
    print("row: ", row, "Col: ", col)


f.close()


arr = sorted(arr)
print(arr)
for i in arr:
    print(i)
ans = 0
for i in range(len(arr)):

    if i == 0:
        continue

    if arr[i] - 1 != arr[i-1]:
        ans = arr[i] - 1


print(ans)
