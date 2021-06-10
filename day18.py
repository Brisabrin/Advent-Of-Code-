f = open("day18.txt", 'r')


res = 0

# ind = 0
s = ''
# cur_sum = 0


def process(ind, track):

    print("hjefk")
    cur_val = 0

    cur_sum = int(s[ind])

    print("ind", ind)

    while ind < len(s):

        print(cur_sum)

        if s[ind] in '*+':
            new_ind = ind + 1

            if s[ind + 1] == '(':

                if s[ind + 2] == '(':
                    cur_val, new_ind = process(ind + 3, False)

                else:
                    cur_val, new_ind = process(ind + 2, False)

                if s[ind] == "*":
                    cur_sum *= cur_val

                else:
                    cur_sum += cur_val

                ind = new_ind

            elif s[ind] == "*":
                # print("hello ", s[ind+1], len(s[ind+1]))

                cur_sum *= int(s[ind+1])

            elif s[ind] == "+":
                cur_sum += int(s[ind+1])

        # elif s[ind] == '(':

        #     cur_val, ind = process(ind + 2, False)

        elif s[ind] == ')' and not track:
            print("yup")
            return cur_sum, ind

        ind += 1
    return cur_sum, ind


for i in f:

    i = i[0:len(i) - 1]
    i = i.replace(' ', '')
    print(i, '\n')
    s = i

    su = 0
    val = 0
    ind = 0

    if s[1] == '(':

        su, ind = process(2, True)
    elif s[0] == '(':

        su, ind = process(1, True)
    else:
        su, ind = process(0, True)

    res += su


f.close()


print(res)
