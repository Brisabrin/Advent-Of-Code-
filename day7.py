import re

bags = {}
vis = {}


def process(s):
    bag_name = []
    s = s.replace("contain", '')
    s = s.replace("bags", '')
    s = s.replace("bag", '')
    s = re.sub(r'\W+', '', s)

    print(s)
    arr_ind = []

    c = ''
    for i in range(len(s)):
        if s[i].isdigit():
            bag_name.append(c)
            arr_ind.append(i)
            # print(c)
            c = ''
        else:
            c += s[i]
    bag_name.append(c)
    # print(c)

    #structure : name = [ ]

    content = bag_name[0]
    bags[content] = []

    vis[content] = False

    for i in range(1, len(bag_name)):
        bags[content].append(bag_name[i])
        vis[bag_name[i]] = False
        bags[content].append(int(s[arr_ind[i-1]]))


co = 0


def dfs(node):
    global co

    val = 1

    # print(node)

    if node in bags:
        for i in range(0, len(bags[node]), 2):

            # print("hfrbihrb")

            ans = dfs(bags[node][i]) * bags[node][i+1]
            val += ans
            print(bags[node][i], ans)

    else:
        return 1

    # print(node, val)
    return val


f = open("day7.txt", "r")

for i in f:
    if bool(re.search(r'\d', i)):
        process(i)


f.close()


node = "shinygold"
print(bags[node])

co = dfs(node)
# for i in bags:
#     print(i, bags[i])

if "brightcrimson" in bags:
    print("yoooo")

# s = "watru2talki,ng4"
# print(re.sub(r'\W+', '', s))
print(co)
