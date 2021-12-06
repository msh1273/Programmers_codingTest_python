from collections import Counter

n = 4
computers = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]

def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i == j: continue
            if computers[i][j] == 1:
                union(parent, i, j)
    for i in range(len(parent)):
        parent[i] = find(parent, i)
    print(parent)
    answer = Counter(parent)
    print(answer)
    return len(answer)

print(solution(n, computers))