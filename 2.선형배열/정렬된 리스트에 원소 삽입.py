def solution(L, x):
    answer = []
    L.append(x)
    L.sort()
    answer = L
    return answer

print(solution([20, 37, 58, 72, 91],65))
