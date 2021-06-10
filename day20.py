from collections import deque
f = open("day20.txt", 'r')

co = 0


arr = [[0 for i in range(100)] for j in range(100)]

# cur_arr = [[0] * 10] * 10
fi = 0
bs = {}

vis = [False] * 4000
m = {}
ind = 0

cur_id = 0

st = 1409

# def update_string():

mac = -1

cx = [-1, 0, 1, 0]
cy = [0, -1, 0, 1]


def flip_string(cur_ind, old, upd, board_string):

    if old == upd:

        a = board_string[cur_ind]

        if old == 0 or old == 2:
            # print("fdsbgu")
            val = board_string[cur_ind][1]
            board_string[cur_ind][1] = board_string[cur_ind][3]
            board_string[cur_ind][3] = val
        else:
            val = board_string[cur_ind][0]
            board_string[cur_ind][0] = board_string[cur_ind][2]
            board_string[cur_ind][2] = val

    else:

        a = deque(board_string[cur_ind])

        mi = old - upd

        if mi > 0:
            mi *= -1

        a.rotate(mi)

        a = list(a)
        board_string[cur_ind] = a


def dfs(x, y, cur_ind, board_string, vis, arr):
    global fi
    print("dfie", cur_ind)

    pos = 0

    if vis[cur_ind]:
        return

    vis[cur_ind] = True

    arr[x][y] = cur_ind
    print(x, y)
    fi += 1
    # print(arr)
    # print("val", arr[49][50])
    # print("val", arr[51][50])

    for i in range(4):
        print(i)

        if arr[x+cx[i]][y+cy[i]] != 0:
            # print(x+cx[i], y+cy[i])
            print("yee")
            continue

        if i == 0:
            pos = 2
        elif i == 1:
            pos = 3

        elif i == 2:
            pos = 0
        else:
            pos = 1

        # v = 0
        s = board_string[cur_ind][i]
        print(s)

        for j in board_string:

            if s in board_string[j] and j != cur_ind:

                flip_string(j, board_string[j].index(s), pos)

                dfs(x + cx[i], y + cy[i], j)

            elif s[::-1] in board_string[j] and j != cur_ind:
                print("fngje")
                flip_string(j, pos, pos)
                dfs(x + cx[i], y + cy[i], j)


for i in f:

    i = i[0: len(i) - 1]

    # print(len(i))
    if len(i) == 0:
        ind = 0

        # print(len(board_string[cur_id][0]))
        # print(len(board_string[cur_id][1]))
        # print(len(board_string[cur_id][2]))
        # print(len(board_string[cur_id][3]))

        continue

    if "Tile" in i:

        cur_id = int(i[5:-1])
        mac = max(cur_id, mac)
        bs[cur_id] = ['', '', '', '']
        ind = 0

        co += 1

    else:

        # print(cur_id, board_string[cur_id])
        # print(i)

        bs[cur_id][1] += i[0]
        bs[cur_id][3] += i[-1]

        if ind == 0:

            for j in i:
                bs[cur_id][0] += j

        elif ind == 9:
            for j in i:
                bs[cur_id][2] += j

        # board_string[]

        ind += 1


f.close()
# print(co)

# print(arr)

dfs(50, 50, st)

# print(arr)
# print(m)
# print(board_string[1409])
print("yee", fi)
