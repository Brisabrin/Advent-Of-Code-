import re
f = open("random.txt", "r")

s = ''
co = 0


di = {"byr": [1920, 2002], "iyr": [2010, 2020],
      "eyr": [2020, 2030]}


def check_valid(wstring):

    posindex = []

    for i in range(len(wstring)):
        if wstring[i] == ":":
            posindex.append(i)

    for i in range(len(posindex)):
        feat = wstring[posindex[i] - 3: posindex[i]]

        val = 0
        if i != len(posindex) - 1:
            val = wstring[posindex[i] + 1:posindex[i+1]]

        else:
            val = wstring[posindex[i] + 1:]
        val = val.strip(' ')
        val = val.strip('\n')

        if feat in di:

            if not(int(val) >= di[feat][0] and int(val) <= di[feat][1]):
                return False

        elif feat == "hgt":

            if "cm" in val:
                val = val[0: len(val) - 2]
                if not(int(val) >= 150 and int(val) <= 193):
                    return False

            elif "in" in val:
                val = val[0: len(val) - 2]
                print(val, "in")

                if not(int(val) >= 59 and int(val) <= 76):
                    return False

            else:
                return False

        elif feat == "hcl":
            if "#" not in val or len(val) != 7:
                return False


for i in f:
    print(len(i))

    if len(i) == 1 or len(i) == 0:
        # print("hello")

        val = s.count(':')

        check_valid(s)

        if val != 8:
            if val == 7 and "cid" not in s:
                co += 1

        else:
            co += 1
        s = ''

    else:
        s = s + i


f.close()
