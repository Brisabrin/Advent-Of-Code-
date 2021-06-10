ang = ["N", "E", "S", "W"]

oppos = {"S": 'N', "N": "S", "E": "W", "W": "E"}

sf = ['E', 'N']
sd = [0, 0]

wf = ['E', 'N']
wd = [10, 1]


f = open("day12.txt", 'r')

for i in f:

    i = i[0: len(i) - 1]

    di = i[0]
    l = int(i[1:])

    if di == 'N' or di == 'E' or di == 'W' or di == 'S':

        if di in wf:

            wd[wf.index(di)] += l

        elif wd[wf.index(oppos[di])] > l:
            wd[wf.index(oppos[di])] -= l

        else:
            wd[wf.index(oppos[di])] = l - wd[wf.index(oppos[di])]
            wf[wf.index(oppos[di])] = di

    elif di == 'R':

        for j in range(2):

            ind = ang.index(wf[j])

            ind = (ind + (l//90)) % 4

            wf[j] = ang[ind]

    elif di == 'L':

        for j in range(2):

            ind = ang.index(wf[j])

            ind = (ind + 4 - (l//90)) % 4

            wf[j] = ang[ind]

    else:

        # first chip dir

        for j in range(2):

            if sf[j] in wf:
                sd[j] += (wd[wf.index(sf[j])]*l)

            elif sd[j] > wd[wf.index(oppos[sf[j]])]*l:

                sd[j] -= wd[wf.index(oppos[sf[j]])]*l

            else:
                sd[j] = wd[wf.index(oppos[sf[j]])]*l - sd[j]
                sf[j] = oppos[sf[j]]


f.close()

print(sd[0] + sd[1])
