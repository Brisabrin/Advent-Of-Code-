arr = [4, 1, 8, 9, 7, 6, 2, 3, 5]
# arr = [3, 8, 9, 1, 2, 5, 4, 6, 7]
mi = min(arr)
ma = max(arr)
st = arr[0]

# for i in range(max(arr) + 1, 1000001):
#     arr.append(i)
print("hek")
cop = arr[:]
for i in range(10000):
    print(i)
    pick_up = arr[arr.index(st)+1: arr.index(st) + 4]
    ind_st = arr.index(st)
    del arr[ind_st + 1: ind_st + 4]

    desti = 0
    # find desti
    diff = 0
    if st == min(arr):
        desti = max(arr)

    else:
        print("ayy")
        print(pick_up)
        desti = st - 1
        print(st)

        for j in pick_up:

            if j == desti:
                desti -= 1

    # print(st, desti)

    if arr.index(desti) > arr.index(st):
        pos = arr.index(desti)
        # print("index", pos, desti)
        arr.insert(pos + 1, pick_up[0])
        arr.insert(pos + 2, pick_up[1])
        arr.insert(pos + 3, pick_up[2])

    else:

        move_arr = arr[0:arr.index(desti)+1]

        move_ind = arr.index(desti)

        del arr[0:move_ind+1]

        for j in move_arr:

            arr.append(j)

        arr.append(pick_up[0])
        arr.append(pick_up[1])
        arr.append(pick_up[2])

    # print(arr)

    if arr == cop:
        print(arr)

    if arr[-1] == st:
        st = arr[0]
    else:
        st = arr[arr.index(st) + 1]


# print(arr)


# s = ''

# for i in range(arr.index(1) + 1, len(arr)):
#     s += str(arr[i])

# for i in range(0, arr.index(1)):
#     s += str(arr[i])
# print(s)
print(arr[arr.index(1)-1])
print(arr[arr.index(1) + 1])
