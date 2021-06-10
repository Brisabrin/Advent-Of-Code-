f = open("day12.txt", "r")

oppos = {"S": 'N', "N": "S", "E": "W", "W": "E"}

cur_face = 'E'

dis = {"N": 0, "E": 0, "S": 0, "W": 0}

ang = ["N", "E", "S", "W"]

for i in f:

    i = i[0:len(i) - 1]
    di = i[0]

    l = int(i[1:])

    if di == 'F':

        if dis[oppos[cur_face]] == 0:
            dis[cur_face] += l

        elif dis[oppos[cur_face]] > l:
            dis[oppos[cur_face]] -= l

        else:
            dis[cur_face] = l - dis[oppos[cur_face]]
            dis[oppos[cur_face]] = 0

    elif di == 'N' or di == 'E' or di == 'W' or di == 'S':

        if dis[oppos[di]] == 0:
            dis[di] += l

        elif dis[oppos[di]] > l:
            dis[oppos[di]] -= l

        else:
            dis[di] = l - dis[oppos[di]]
            dis[oppos[di]] = 0

    elif di == 'R':

        ind = ang.index(cur_face)

        ind = (ind + (l//90)) % 4

        cur_face = ang[ind]

    elif di == 'L':

        ind = ang.index(cur_face)

        ind = (ind + 4 - (l//90)) % 4

        cur_face = ang[ind]


f.close()

res = 0

for i in dis:
    res += dis[i]

print(res)
