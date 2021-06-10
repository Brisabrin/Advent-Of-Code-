import re
f = open('puzzle.txt', 'r')

# print(f.readline())


def valid(mi, ma, s, ch) -> bool:

    co = 0
    for i in s:

        if i == ch:
            co += 1

    if co >= mi and co <= ma:
        return True
    return False


finalco = 0
for i in f:
    mi = int(re.findall('\d+', i)[0])
    ma = int(re.findall('\d+', i)[1])

    ind = i.find(':')

    ch = i[ind-1]

    s = i[ind + 1:]

    print(s)

    if valid(mi, ma, s, ch):
        finalco += 1


# locate the index of digits


f.close()

print(valid(1, 3, "abcde", 'a'))
print(valid(1, 3, "cdefg", 'b'))
print(valid(2, 9, "ccccccccc", 'c'))

print(finalco)
