import collections
f = open("day22.txt", 'r')

player_2 = []
player_1 = []

two_track = False

for i in f:

    if len(i) == 1:
        continue

    if "Player" in i:

        if "Player 2" in i:
            two_track = True

        continue

    i = i[0: len(i) - 1]
    if not two_track:

        player_1.append(int(i))

    else:

        player_2.append(int(i))


f.close()


player_1 = collections.deque(player_1)
player_2 = collections.deque(player_2)

track = True

while track:

    fi = player_1.popleft()
    se = player_2.popleft()

    if fi > se:

        player_1.append(fi)
        player_1.append(se)

    else:
        player_2.append(se)
        player_2.append(fi)

    if len(player_1) == 0 or len(player_2) == 0:

        track = False


res = 0

if len(player_1) != 0:

    player_1 = list(player_1)
    for i in range(0, len(player_1)):

        res += (len(player_1) - i) * player_1[i]

print(res)
