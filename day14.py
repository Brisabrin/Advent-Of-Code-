f = open("day14.txt", 'r')

bm = ''
arr = []
mem = {}
val = 0

pos = []
s = ''
some = 0


def change_bin(ind, n, su):
    print("hello")

    if ind == n:

        mem[some+su] = val
        return

    # set to 0
    change_bin(ind + 1, n, su)

    # set to 1
    change_bin(ind + 1, n, su + (2**(len(s) - pos[ind]-1)))


for i in f:

    i = i[0: len(i) - 1]

    if 'X' in i:
        bm = i[7:]

    else:
        some = 0
        pos = []

        val = int(i[i.index('=') + 1:])
        address = int(i[i.index('[') + 1: i.index(']')])

        bin_val = bin(address)[2:].zfill(len(bm))

        mask = bm
        # print("mask", mask)
        # print("bin_val", bin_val)
        s = ''

        for j in range(0, len(mask)):

            if mask[j] == 'X':
                s = s + 'X'
                pos.append(j)

            elif mask[j] == '0':
                s = s + bin_val[j]

            else:
                s = s + mask[j]

            if s[j] == '1':

                some += (2**(len(mask) - j - 1))

        print(s)
        print(some)

        # res = int(s, 2)
        # print(s)

        change_bin(0, len(pos), 0)


f.close()


# print(int(bin(13), 2))
ans = 0

for i in mem:
    ans += mem[i]

print(ans)

# print(mem)
