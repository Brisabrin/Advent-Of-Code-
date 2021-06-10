import re
f = open("day16.txt", 'r')


nearby = False
your_ticket = False


mi = 1e10
ma = -1

ans = 0

# range type
m = {}
co = 0

ticket_type = {}
line_co = 0

ticket_grp = {}


#  key = the type index ,value =  array containnig possible types it fits in
# to ( index of the types)
posib_match = {}
match = {}

your_ticket_arr = []

for i in range(20):
    ticket_type[i] = []
    m[i] = []
    posib_match[i] = []
    ticket_grp[i] = []
    match[i] = []


for i in f:

    if "nearby tickets" in i:
        nearby = True
    elif "your ticket" in i:
        your_ticket = True

    elif your_ticket == True and nearby == False and len(i) > 1:
        your_ticket_arr = list(map(int, re.findall(r'\d+', i)))

        continue

    elif nearby == False:

        arr = list(map(int, re.findall(r'\d+', i)))
        print("yesy", line_co)
        for j in range(0, len(arr), 2):
            print("start", arr[j])
            st = arr[j]
            en = arr[j+1]

            m[line_co].append(st)
            m[line_co].append(en)

            if mi == 1e10:
                mi = st
                ma = en

            else:

                if st < mi and en >= mi - 1:
                    mi = st

                if en > ma and st <= en + 1:
                    ma = en

    else:
        arr = list(map(int, re.findall(r'\d+', i)))

        for j in range(0, len(arr)):
            if arr[j] >= mi and arr[j] <= ma:

                ticket_type[j].append(arr[j])

    line_co += 1


f.close()


# print(ans)

# print(co)

# print(m)

for i in range(20):

    for j in range(20):
        # print(m)
        st1 = m[j][0]
        en1 = m[j][1]
        st2 = m[j][2]
        en2 = m[j][3]
        track = True
        for k in ticket_type[i]:
            if (k >= st1 and k <= en1) or (k >= st2 and k <= en2):
                continue

            else:

                # print(st1, en1, k)
                track = False

        if track:
            posib_match[i].append(j)
            ticket_grp[j].append(i)


# print()
# print()

print(posib_match)

# print(ticket_type)

co = 20

while co > 0:

    for i in range(20):
        if len(posib_match[i]) == 0:
            continue

        if len(posib_match[i]) == 1:

            match[posib_match[i][0]] = i

            co -= 1

            grp_index = posib_match[i][0]

            for j in ticket_grp[grp_index]:
                posib_match[j].remove(grp_index)

            posib_match[i] = []


print(match)


print(your_ticket_arr)


fin = 1

for i in range(6):

    pos = match[i]

    fin *= your_ticket_arr[pos]


print(fin)
