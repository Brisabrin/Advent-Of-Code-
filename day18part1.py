f = open("day18.txt", 'r')
s = ''
res = 0


def process(ind, track):

    cur_sum = 0
    cur_val = 0
    # print("ye")
    # print(cur_sum)

    while ind < len(s):
        print(cur_sum)

        if s[ind] in '*+':
            new_ind = ind + 1

            if s[ind+1] == '(':

                cur_val, new_ind = process(ind + 1, False)

                if s[ind] == "*":
                    cur_sum *= cur_val
                    # print("cur_sum", cur_sum, "cur val", cur_val)

                else:
                    cur_sum += cur_val

                ind = new_ind

            elif s[ind] == "*":
                # print("hello ", s[ind+1], len(s[ind+1]))

                cur_sum *= int(s[ind+1])

            elif s[ind] == "+":
                cur_sum += int(s[ind+1])

        elif cur_sum == 0 and s[ind].isdigit():
            # print("dhnjengfjoenrfjkn")
            cur_sum = int(s[ind])

        elif s[ind] == '(' and s[ind+1] == '(':

            cur_val, new_ind = process(ind + 1, False)
            # print(cur_val, new_ind)

            cur_sum = cur_val
            ind = new_ind

        elif s[ind] == ')' and not track:
            # print("yup")
            return cur_sum, ind

        ind += 1

    return cur_sum, ind


for i in f:

    i = i[0: len(i) - 1]

    i = i.replace(' ', '')
    s = i
    print(i, '\n')

    su = 0
    val = 0
    ind = 0
    # print(ind)

    su, ind = process(0, True)
    print("final", su)

    res += su


f.close()

print(res)
