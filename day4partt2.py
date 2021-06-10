f = open("day4.txt", 'r')


# # extract the key: pair values


def check_valid(wstring):
    print("break\n\n")
    print(wstring)
    wstring = wstring.replace('\n', ' ')

    wstring = wstring.split(' ')
    print(wstring)

    for i in wstring:
        # print(i)
        if len(i) == 0:
            continue

        feat = i[0:3]
        val = i[4:len(i)]
        print(feat, val)
        print(len(feat), len(val))

        if feat == "byr" and not(int(val) >= 1920 and int(val) <= 2002):
            print("Wrong")
            return False

        elif feat == "iyr" and not(int(val) >= 2010 and int(val) <= 2020):
            print("Wrong")
            return False
        elif feat == "eyr" and not(int(val) >= 2020 and int(val) <= 2030):
            print("Wrong")
            return False

        elif feat == "hgt":

            if "cm" in val:
                val = val[0: len(val) - 2]
                if not(int(val) >= 150 and int(val) <= 193):
                    print("Wrong")
                    return False

            elif "in" in val:
                val = val[0: len(val) - 2]
                if not(int(val) >= 59 and int(val) <= 76):
                    print("Wrong")
                    return False

            else:
                print("Wrong")
                return False

        elif feat == "hcl":
            if not(val[0] == "#" and len(val) == 7):
                print(val[0])
                print("Wrong")
                return False

            comp = "#0123456789abcdef"

            for j in val:
                if j not in comp:
                    print("Wrong")
                    return False

        elif feat == "ecl":
            if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                print("Wrong")
                return False

        elif feat == "pid":
            # check for leading zeros

            if len(val) != 9:
                print("Wrong")
                return False
    print("YOUR ARE RIGHT ")
    return True


co = 0
s = ''
for i in f:
    # print(len(i))

    if len(i) == 1 or len(i) == 0:
        # print("hello")

        val = s.count(':')
        # print(s)

        # check_valid(s)

        if check_valid(s) and ((val == 7 and ("cid" not in s)) or val == 8):
            co += 1
            # print("hdjeh")

        # if val != 8:
        #     if val == 7 and "cid" not in s:
        #         co += 1

        # else:
        #     co += 1
        s = ''

    else:
        s = s + i

# s = ''

# for i in f:

#     if len(i) == 1:
#         s = s.replace("\n", ' ')
#         wstring = s.split(' ')
#         print(wstring)

#     else:
#         s = s + i


f.close()
print(co)
