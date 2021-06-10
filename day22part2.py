import collections
f = open("day22.txt", 'r')


two_track = False

outer_track = False
p1 = []
p2 = []

c = 1


def rec(prev1, prev2, player_1, player_2, first, co):
    global c
    win = 0
    # global outer_track

    # if outer_track:

    # return

    # check before drawing card

    inner_track = True

    while inner_track:
        ro = False
        print("game : ", co)
        # print(player_1)
        # print(player_2)

        if list(player_1) in prev1[0:-1] or list(player_2) in prev2[0:-1]:
            print(player_1, prev1[0:-1])
            print(player_2, prev2[0:-1])
            # outer_track = True
            win = 1
            if first:
                # print("hefj")
                return win, player_1

            return win

        fi = player_1.popleft()
        se = player_2.popleft()

        if (fi <= len(player_1)) and (se <= len(player_2)):
            cop1 = collections.deque(list(player_1)[0:fi])
            cop2 = collections.deque(list(player_2)[0:se])

            c += 1
            win = rec([list(player_1)], [list(player_2)], cop1, cop2, False, c)
            # print("up", win)
            ro = True

        if not ro:

            if fi > se:

                player_1.append(fi)
                player_1.append(se)

            else:
                player_2.append(se)
                player_2.append(fi)

        elif win == 1:
            player_1.append(fi)
            player_1.append(se)

        elif win == 2:
            player_2.append(se)
            player_2.append(fi)

        prev1.append(list(player_1))
        prev2.append(list(player_2))

        if len(player_1) == 0 or len(player_2) == 0:

            inner_track = False

            if len(player_1) == 0:
                win = 2
            else:
                win = 1
            # print("hello", win)
            break

    if first:

        if win == 1:
            return 1, player_1

        else:
            return 2, player_2

    return win


for i in f:

    if len(i) == 1:
        continue

    if "Player" in i:

        if "Player 2" in i:
            two_track = True

        continue

    i = i[0: len(i) - 1]
    if not two_track:

        p1.append(int(i))

    else:

        p2.append(int(i))


f.close()


p1 = collections.deque(p1)
p2 = collections.deque(p2)

w, arr = rec([], [], p1, p2, True, 1)

print(w, arr)

res = 0


arr = list(arr)
for i in range(0, len(arr)):

    res += (len(arr) - i) * arr[i]

print(res)
