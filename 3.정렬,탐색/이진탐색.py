def solution(L, x):
    answer = -1
    lower = 0
    upper = len(L) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            answer = middle
            return answer
        elif L[middle] < x:
            lower = middle + 1
        elif L[middle] > x:
            upper = middle - 1

    return answer


print(solution([2, 3, 5, 6, 9, 11, 15], 6))
print(solution([2, 5, 7, 9, 11], 4))
print(solution([1, 2, 3], 3))
