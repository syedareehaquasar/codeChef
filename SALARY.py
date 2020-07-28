def solution(elements, n):
    return sum(elements) - n * min(elements)


tc = int(input())
while tc > 0:
    n = int(input())
    elements = list(map(int, input().split()))
    print(solution(elements, n))
    tc -= 1