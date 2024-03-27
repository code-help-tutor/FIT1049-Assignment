WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def post_time(graph, path):
    newlist = []
    for i in range(len(path)-1):
        newlist.append(graph[path[i]][path[i+1]])
    return sum(newlist)


def post_route(graph):
    route = [0]
    newroute = [0]
    for _ in range(len(graph)-1):
        chgraph = graph[route[-1]]
        mn = max(chgraph)
        alist = []
        for a in range(len(graph)):  # items are the same
            if a not in route:
                if chgraph[a] == mn:
                    alist.append(a)
        if len(alist) > 0:
            newroute.append(alist[0])
        for i in range(len(graph)):  # items are different
            if i not in route:
                if chgraph[i] < mn:
                    mn = chgraph[i]
                    newroute.append(i)
        route.append(newroute[-1])
    route.append(0)
    return route


def on_time(graph, days):
    # code permutation,lex_suc, is adapted from lecture 11, Slides 53 & 54
    def permutations(a, b):
        first = list(range(a, b))
        last = list(reversed(first))
        res = [first]
        while res[-1] != last:
            res += [lex_suc(res[-1])]
        return res

    def lex_suc(perm):
        n = len(perm)
        res = perm[:]
        for i in range(n-2, -1, -1):
            if perm[i] < perm[i+1]:
                break
        for j in range(n-1, i, -1):
            if perm[j] > perm[i]:
                break
        res[i], res[j] = res[j], res[i]
        return res[:i+1] + list(reversed(res[i+1:]))

    all = permutations(1, len(graph))
    opt = [0] + all[0]
    for tour in all:
        if post_time(graph, [0] + tour) < post_time(graph, opt):
            opt = [0] + tour
    # here is the end of cited part
    opt.append(0)
    day = post_time(graph, opt)
    if day <= days:
        return True
    else:
        return False


postage1 = [[0, 1, 1, 3, 2],
            [1, 0, 4, 5, 1],
            [1, 4, 0, 1, 3],
            [3, 5, 1, 0, 1],
            [2, 1, 3, 1, 0]]

postage2 = [[0, 2, 2, 1, 2],
            [2, 0, 1, 1, 2],
            [2, 1, 0, 1, 4],
            [1, 1, 1, 0, 1],
            [2, 2, 4, 1, 0]]

print(post_time(postage1, [0, 1, 4, 3, 2, 0]))
print(post_time(postage1, [0, 3, 1, 2, 3]))
print(post_route(postage1))
print(post_route(postage2))
print(on_time(postage1, 5))
print(on_time(postage2, 8))
print(on_time(postage2, 5))
