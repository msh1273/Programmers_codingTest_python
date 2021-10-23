from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    count = 0

    return count

def bfs(numbers, target):
    count = 0
    _sum = 0
    queue = deque()
    queue.append([-numbers[0], 0])
    queue.append([+numbers[0], 0])
    n = len(numbers)

    while queue:
        _sum, i = queue.popleft()
        if i+1 == n:
            if _sum == target:
                count += 1
        else:
            queue.append([_sum-numbers[i+1], i+1])
            queue.append([_sum+numbers[i+1], i+1])
    return count

print(bfs(numbers,target))