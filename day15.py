arr = [10, 16, 6, 0, 1, 17]
m = {}

# def find_latest_index(ind):

#     for j in range(ind - 1, -1, -1):

#         if arr[j] == arr[ind]:
#             return j
#     return ind

f = open("day15.txt", 'r')

for i in f:

    ke = int(i[0:i.index(":")])
    va = int(i[i.index(":") + 1: len(i) - 1 ])
    m[ke] = va

    # pre_val = 264391
f.close()
pre_val = 3065083

#pre_val = 264391

for i in range(10000000):

    print(i)
    # if i < len(arr):
    #     m[arr[i]] = i
    #     # print(arr[i])
    #     continue

    val = 0
    if pre_val not in m:
        m[pre_val] = i - 1
        val = i - 1

    else:
        val = m[pre_val]

    # arr.append(i - 1 - val)

    m[pre_val] = i-1
    pre_val = i - 1 - val
    # print(i-1-val)

    # arr.append(i - 1 - val)
f = open("day15.txt", 'r+')
f.truncate(0)
f.close()
f = open("day15.txt", 'w')

for i in m:
    f.write(str(i)+":"+str(m[i])+'\n')

f.close()


print(pre_val)


# f = open("day15.txt", 'w')

# f.write("hello")

# f.close()
