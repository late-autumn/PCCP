# Fibonacci 순열은 아래와 같이 정의됩니다.
# F0 = 0
# F1 = 1
# Fn = Fn - 1 + Fn - 2, n >= 2

def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x - 1) + solution(x - 2)


print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))