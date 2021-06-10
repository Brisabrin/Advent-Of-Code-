f = open('random.txt', 'r')

arr = [False] * 3000

co = 0
ans = 0
for i in f:

    s = int(i[0:len(i)-1])
    # print(s)

    arr[s] = True

    if(arr[2020 - s]):
        co += 1
        ans = (2020 - s) * s


f.close()


print(ans)
