def solution(x):
    answer = 0
    answer += x[0] + x[-1]
    return answer

print(solution([5, 3, 8, 2]))