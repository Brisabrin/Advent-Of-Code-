arr = []
f = open("day10.txt", 'r')

for i in f:
    i = i[0:len(i) - 1]

    i = int(i)

    arr.append(i)


f.close()

arr.append(0)
arr = sorted(arr)

arr.append(arr[len(arr) - 1] + 3)


dp = [0] * len(arr)
dp[0] = 1


for i in range(1, len(arr)):

    for j in range(0,  i):

        if arr[i] - arr[j] <= 3:
            dp[i] += dp[j]

print(dp[len(arr) - 1])
