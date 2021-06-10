f = open("day11.txt", 'r')

line_co = 0
arr = []
cop = []
n = 0
m = 0


def check_equal():
    for i in range(n):
        for j in range(m):

            if arr[i][j] != cop[i][j]:
                print(arr[i][j], cop[i][j])
                print(i, j, "hello")
                return False

    return True


def check_bool(i,  j):
    if (i >= 0 and i < n) and (j >= 0 and j < m):
        return True

    return False


def bfs(i,  j, cx, cy):

    while check_bool(i,  j):

        if arr[i][j] == 'L':
            return False

        elif arr[i][j] == '#':
            return True
        i = i + cx
        j = j + cy

    return False


for i in f:
    i = i[0: len(i) - 1]
    for j in range(0, len(i)):
        if j == 0:
            arr.append([])
        arr[line_co].append(i[j])
    line_co += 1


# print(arr)
f.close()
n = len(arr)
m = len(arr[0])
# print(n, m, "ello")
cx = [0, 0, 1, 1, 1, -1, -1, -1]
cy = [1, -1, 0, 1, -1, 0, 1, -1]

track = True
ans = 0

while track:
    cop = list(map(list, arr))
    for i in range(n):
        for j in range(m):
            # print(arr[i][j])
            co = 0
            bfs_track = 0

            if arr[i][j] != '.':
                print(i,  j)

                for k in range(8):
                    newx = i + cx[k]
                    newy = j + cy[k]

                    if check_bool(newx, newy):
                        # print(cx[k], cy[k])

                        if bfs(newx, newy, cx[k], cy[k]):
                            print("hello")
                            bfs_track += 1

                # if co == 0 and arr[i][j] == 'L':
                #     cop[i][j] = '#'

                print("stuff", bfs_track)

                if bfs_track >= 5 and arr[i][j] == '#':
                    # print("ddfvdrgrdg")

                    cop[i][j] = 'L'

                elif arr[i][j] == 'L' and bfs_track == 0:
                    # print("yay")
                    cop[i][j] = '#'

                else:
                    cop[i][j] = arr[i][j]

                # print(i, j, ": ", bfs_track)

    print()
    print("cop", cop)
    if check_equal():
        print("yes")
        for i1 in range(n):
            for j1 in range(m):

                if arr[i1][j1] == '#':
                    ans += 1

        track = False

    else:
        arr = list(map(list, cop))
        print("arr", arr)


print(ans)
