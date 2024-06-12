# 빈칸 채우기

def solution(L, x, l, u):
    if l > u:  # 빈칸
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)  # 빈칸
    else:
        return solution(L, x, mid + 1, u)  # 빈칸


print(solution([2, 3, 5, 6, 9, 11, 15], 6, 0, 6))
print(solution([2, 5, 7, 9, 11], 4, 0, 4))
