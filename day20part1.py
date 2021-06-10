from collections import deque
f = open('random.txt', 'r')
bs = {}
mac = 0
co = 0
a = [[0 for i in range(50)] for j in range(50)]
string_occur = {}
cur_id = 0
v = {}

pos = {0: [-1, 0], 1: [0, -1], 2: [1, 0], 3: [0,  1]}


def flip(old,  cur_ind, s):

    if old == 0:
        upd = 2
    elif old == 2:
        upd = 0
    elif old == 1:
        upd = 3
    elif old == 3:
        upd = 1

    if bs[cur_ind].index(s) == upd:
        return

    if old == upd:

        a = bs[cur_ind]

        if old == 0 or old == 2:
            # print("fdsbgu")
            val = bs[cur_ind][1]
            bs[cur_ind][1] = bs[cur_ind][3]
            bs[cur_ind][3] = val
        else:
            val = bs[cur_ind][0]
            bs[cur_ind][0] = bs[cur_ind][2]
            bs[cur_ind][2] = val

    else:

        a = deque(bs[cur_ind])

        mi = old - upd

        if mi > 0:
            mi *= -1

        a.rotate(mi)

        a = list(a)
        bs[cur_ind] = a


def dfs(x, y, cur_ind):

    c = 0

    a[x][y] = cur_ind

    while c < co:

        v[cur_ind] = True

        c += 1

        for i in range(0,  len(bs[cur_ind])):

            if len(string_occur[bs[cur_ind][i]]) == 2:

                next_id = 0
                if string_occur[bs[cur_ind][i]][0] == cur_ind:
                    next_id = string_occur[bs[cur_ind][i]][1]

                else:
                    next_id = string_occur[bs[cur_ind][i]][0]

                if not v[next_id]:

                    flip(i,  next_id, bs[cur_ind][i])  # modify bs
                    newx = x + pos[i][0]
                    newy = y + pos[i][1]

                    dfs(newx, newy, next_id)

    return


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
        # co += 1
        if cur_id != 0:
            print(bs[cur_id][0])
            print(bs[cur_id][1])
            print(bs[cur_id][2])
            print(bs[cur_id][3])
            print()
            if bs[cur_id][1] in string_occur:
                string_occur[bs[cur_id][1]].append(cur_id)
            else:
                string_occur[bs[cur_id][1]] = [cur_id]
            if bs[cur_id][3] in string_occur:
                string_occur[bs[cur_id][3]].append(cur_id)
            else:
                string_occur[bs[cur_id][3]] = [cur_id]
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
            if bs[cur_id][0] in string_occur:
                string_occur[bs[cur_id][0]].append(cur_id)
            else:
                string_occur[bs[cur_id][0]] = [cur_id]
        elif ind == 9:
            for j in i:
                bs[cur_id][2] += j

            if bs[cur_id][2] in string_occur:
                string_occur[bs[cur_id][2]].append(cur_id)
            else:
                string_occur[bs[cur_id][2]] = [cur_id]
        # board_string[]
        ind += 1
f.close()
if bs[cur_id][1] in string_occur:
    string_occur[bs[cur_id][1]].append(cur_id)
else:
    string_occur[bs[cur_id][1]] = [cur_id]
if bs[cur_id][3] in string_occur:
    string_occur[bs[cur_id][3]].append(cur_id)
else:
    string_occur[bs[cur_id][3]] = [cur_id]
print(co)

for i in bs:
    v[i] = False
# dfs(a, v)

print(string_occur)

# a2 = list(map(list, a))


# dfs(a , v.copy() , 25 , 25  )
dfs()
