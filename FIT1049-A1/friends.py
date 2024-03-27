WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def popular(graph_list, n):
    frd = []
    for i in range(len(graph_list)):
        if len(graph_list[i]) >= n:
            frd.append(i)
    print(frd)


clayton_list = [[1,2,3],[0,3],[0,4],[0,1],[2]]
print(popular(clayton_list,2))
print(popular(clayton_list,3))
print(popular(clayton_list,0))


def foaf(graph_matrix, person1, person2):
    outcome = False
    for i in range(len(graph_matrix)):
        if graph_matrix[person1][i] == graph_matrix[person2][i] == 1 and graph_matrix[person1][person2] == 0:
            #they are not friends and they have common friends
            outcome = True
    return outcome


def society(graph_matrix, person):
    friend = []
    newlist = ""
    if sum(graph_matrix[person]) >= 2:
        newlist = graph_matrix[person]
        for i in range(len(newlist)):
            if newlist[i] == 1:
                friend.append(i)
    for i in range(len(friend)):
        if graph_matrix[friend[0]][friend[i]] == 1:
            return True
    else:
        return False


clayton_matrix = [[0, 1, 1, 1, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 0, 1],
                  [1, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0]]


print(foaf(clayton_matrix,0,4))
print(foaf(clayton_matrix,0,3))
print(foaf(clayton_matrix,1,4))


print(society(clayton_matrix, 0))
print(society(clayton_matrix, 2))