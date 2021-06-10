f = open("day9.txt", "r")

prefix_sum = [0]
val = [0]

line_co = 1


for i in f:

    i = i[0:len(i) - 1]
    # print(i)
    i = int(i)

    prefix_sum.append(prefix_sum[line_co - 1] + i)

    val.append(i)
    line_co += 1

f.close()

# for i in prefix_sum:
#     print(i)

st = 0
en = 0

for i in range(len(prefix_sum)):
    for j in range(i + 1, len(prefix_sum)):
        # print(i, j)

        res = prefix_sum[j] - prefix_sum[i]

        if res == 1309761972:
            # if res == 127:
            # print("yay")

            if j - i >= 2:
                st = i + 1
                en = j
                break

print(st, en)
res = []
for i in range(st, en + 1):
    res.append(val[i])


print(max(res) + min(res))
