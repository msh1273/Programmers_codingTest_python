sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    width =[]
    height = []
    for w,h in sizes:
        if w < h:
            temp = w
            w = h
            h = temp
        width.append(w)
        height.append(h)
    return max(width)*max(height)

print(solution(sizes))