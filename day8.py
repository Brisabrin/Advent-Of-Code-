f = open("random.txt", 'r')

inst = []
vis = []

co = 0

acc = 0
for i in f:

    if '\n' in i:
        i = i[0: len(i) - 1]
    else:
        i = i[0:len(i)]

    inst.append(i)
    vis.append(False)


track = True
line_co = 0

# for i in inst:
#     print(i)

while track:
    print(line_co)
    print(inst[line_co])

    if vis[line_co]:
        track = False
        break

    vis[line_co] = True

    if "acc" in inst[line_co]:
        print("acc")
        sign = inst[line_co][4]
        val = int(inst[line_co][5:])

        if sign == "+":
            acc += val
        else:
            acc -= val

        line_co += 1

    elif "jmp" in inst[line_co]:
        print("jmp")
        sign = inst[line_co][4]
        val = int(inst[line_co][5:])

        if sign == "+":
            line_co += val
        else:
            line_co -= val

    else:
        line_co += 1


print(acc)
f.close()
