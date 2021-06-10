arr = [[0 for x in range(100)] for y in range(100)]

# deep copy array

f = open("day24.txt", 'r')

coord = {'e': [0, 2], 'w': [0, -2], 'se': [1, 1], 'nw': [-1, -1],
         'sw': [1, -1], 'ne': [-1, 1]}

cx = []
cy = []


for i in coord:

    cx.append(coord[i][0])
    cy.append(coord[i][1])


for i in f:

    i = i[0:len(i) - 1]

    st = 50
    en = 50

    s = ''
    for j in i:

        if s != '':
            s += j
            st += coord[s][0]
            en += coord[s][1]
            s = ''

        elif j in 'sn':
            s = j

        else:

            st += coord[j][0]
            en += coord[j][1]

    arr[st][en] ^= 1

    print(arr[st][en])

f.close()
co = 0

for i in range(100):
    for j in range(100):

        if arr[i][j]:
            co += 1
print(co)
