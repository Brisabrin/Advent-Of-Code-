import re
f = open('puzzle.txt', 'r')


def valid(mi, ma, s, ch):
    mi -= 1
    ma -= 1
    if (s[mi] != ch and s[ma] != ch) or (s[mi] == ch and s[ma] == ch):
        return False

    return True


finalco = 0
for i in f:
    mi = int(re.findall('\d+', i)[0])
    ma = int(re.findall('\d+', i)[1])

    ind = i.find(':')

    ch = i[ind-1]

    s = i[ind + 2: len(i) - 1]
    print(len(s))

    # print("{},{},{},{}".format(str(mi), str(ma), s, valid(mi, ma, s, ch)))

    # print(s + " " + valid(mi, ma, s, ch))

    if valid(mi, ma, s, ch) == False:
        continue

    finalco += 1


f.close()
print(finalco)

print(valid(1, 3, "abcde", 'a'))
print(valid(1, 3, "cdefg", 'b'))
print(valid(2, 9, "ccccccccc", 'c'))
