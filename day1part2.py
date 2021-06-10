f = open("random.txt", 'r')


arr = []

for i in f:

    s = int(i[0:len(i)-1])

    arr.append(s)


ans = 0

for i in range(len(arr)):

    for j in range(i, len(arr)):

        for k in range(j, len(arr)):

            if arr[i] + arr[j] + arr[k] == 2020:
                ans = arr[i] * arr[j] * arr[k]

print(ans)


f.close()
