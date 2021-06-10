f = open("day13.txt", 'r')

cur_time = 0
arr = []

for i in f:

    i = i[0:len(i)-1]

    if ',' not in i:
        continue

    s = ''
    for j in i:

        if j == ',':
            if s == 'x':
                arr.append(int(0))

            else:
                arr.append(int(s))

            s = ''

        else:
            s = s + j
    arr.append(int(s))

f.close()

print(arr)

ans = arr[0] - 1

track = True

print("helo")
print(arr)
print(len(arr))

shift = {}


for i in arr:

    if i == 0:
        continue

    shift[i] = arr.index(i)

b = []
for i in arr:

    if i != 0:
        b.append(i)

print(b)

b.sort()
b.reverse()
print(b)

track = True

ans = (600000000000000 // b[0]) * b[0]

print(shift)

mul = 1

for i in b:
    mul *= i

val = 500000000000000

res = val

it = []

for i in shift:

    if shift[i] != 0:
        res *= (val + shift[i])

    it.append(shift[i])


print(res//mul)

di = res // mul


while track:

    prod = di * mul

    a = (prod // 9) - it[-1]
    inner_track = True
    mult = 1

    print(a)
    while inner_track:

        for i in shift:
            mult *= (a + shift[i])

        if mult == prod:
            print("yay", a)
            inner_track = False
            track = False

        elif mult > prod:
            inner_track = False

            # while track:

            #     inner_track = True
            #     print(ans)
            #     for i in range(1, len(b)):

            #         time_after = ans + (shift[b[i]] - shift[b[0]])

            #         if time_after % b[i] == 0:
            #             continue

            #         else:
            #             inner_track = False

            #     if inner_track == True:
            #         print(ans)
            #         track = False

            #     ans +=

