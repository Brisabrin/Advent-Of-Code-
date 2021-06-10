f = open("day6.txt", "r")


def unique_count(s, num_count):

    arr = [0] * 26
    co = 0

    for i in s:
        # print(ord(i) - 97)

        arr[ord(i) - 97] += 1

    # print(co)

    for i in arr:
        if i == num_count:
            co += 1

    return co


ans = 0
s = ''
num_count = 0

for i in f:
    print(len(i))

    if len(i) == 1:
        ans += unique_count(s, num_count)
        # print(s)
        s = ''
        num_count = 0

    else:
        s = s + i[0:len(i) - 1]
        num_count += 1

f.close()
print(ans)
