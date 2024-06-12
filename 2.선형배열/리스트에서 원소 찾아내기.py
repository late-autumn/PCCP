def solution(L, x):
    answer = []

    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer

def anotherFunction(L,x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]

print(solution([64, 72, 83, 72, 54], 72))