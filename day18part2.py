f = open("day18.txt", 'r')

res = 0


def process(ind, track):

    # cur_sum = 0
    # cur_val = 0

    exp = []
    cur_sum = 1
    print("dhfejrnbgjo")

    while ind < len(s):
        # print("ind", ind)

        # print(cur_sum)

        if s[ind] in '*+':

            exp.append(s[ind])

            new_ind = ind + 1

            if s[ind+1] == '(':

                cur_val, new_ind = process(ind + 2, False)

                exp.append(cur_val)

                ind = new_ind

        elif s[ind].isdigit():
            exp.append(int(s[ind]))

        elif s[ind] == '(':

            if s[ind + 1] == '(':
                cur_val, new_ind = process(ind + 2, False)

            else:
                cur_val, new_ind = process(ind + 1, False)
            exp.append(cur_val)
            ind = new_ind

        elif s[ind] == ')' and not track:

            cur_sum = 1

            new_exp = [exp[0]]

            calc_ind = 1
            print(exp)

            while calc_ind < len(exp):

                if exp[calc_ind] == '*':

                    # new_exp.append(exp[calc_ind - 1])
                    # new_exp.append(exp[calc_ind] )

                    new_exp.append(exp[calc_ind + 1])

                elif exp[calc_ind] == '+':

                    new_exp[- 1] = new_exp[-1] + exp[calc_ind + 1]

                calc_ind += 2

            print(new_exp)
            for i in new_exp:
                cur_sum *= i

            print("cursum ", cur_sum)
            print("yea went")

            return cur_sum, ind

        elif s[ind] == ')':

            cur_sum = 1

            new_exp = [exp[0]]

            calc_ind = 1
            # print(exp)

            while calc_ind < len(exp):

                if exp[calc_ind] == '*':

                    # new_exp.append(exp[calc_ind - 1])
                    # new_exp.append(exp[calc_ind] )

                    new_exp.append(exp[calc_ind + 1])

                elif exp[calc_ind] == '+':

                    new_exp[- 1] = new_exp[-1] + exp[calc_ind + 1]

                calc_ind += 2

            # print(new_exp)
            for i in new_exp:
                cur_sum *= i

            exp = []

            exp.append(cur_sum)

        ind += 1

    cur_sum = 1

    new_exp = [exp[0]]

    calc_ind = 1
    # print(exp)

    while calc_ind < len(exp):

        if exp[calc_ind] == '*':

            # new_exp.append(exp[calc_ind - 1])
            # new_exp.append(exp[calc_ind] )

            new_exp.append(exp[calc_ind + 1])

        elif exp[calc_ind] == '+':

            new_exp[- 1] = new_exp[-1] + exp[calc_ind + 1]

        calc_ind += 2

    print(new_exp)
    for i in new_exp:
        cur_sum *= i

    print("yea went")

    return cur_sum, ind

# 1 * 3 + 4 + 8


for i in f:

    i = i[0: len(i) - 1]

    i = i.replace(' ', '')
    s = i
    print("yup", i, '\n')

    su = 0
    val = 0
    ind = 0
    # print(ind)

    su, ind = process(0, True)
    print("final", su)

    res += su


f.close()

print(res)
