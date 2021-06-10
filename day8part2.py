f = open("day8.txt", 'r')

inst = []
vis = []
jmp = []
co = 0
acc = 0

for i in f:

    if '\n' in i:
        i = i[0: len(i) - 1]

    else:
        i = i[0:len(i)]

    inst.append(i)
    vis.append(False)

    if "jmp" in i:
        jmp.append(co)

    co += 1

print(jmp)
the_one = 0

for i in jmp:

    for j in range(len(vis)):
        vis[j] = False
    track = True
    line_co = 0

    acc = 0
    while track and line_co < len(inst):

        if vis[line_co]:
            track = False
            break

        vis[line_co] = True

        if "acc" in inst[line_co]:
            # print("acc")
            sign = inst[line_co][4]
            val = int(inst[line_co][5:])

            if sign == "+":
                acc += val
            else:
                acc -= val

            line_co += 1

        elif "jmp" in inst[line_co] and line_co != i:
            print("jmp")
            sign = inst[line_co][4]
            val = int(inst[line_co][5:])

            if sign == "+":
                line_co += val
            else:
                line_co -= val

        else:
            line_co += 1

    if track:
        print("yay", i, acc)
        the_one = i
        break


# print(acc)
print(the_one)

f.close()
