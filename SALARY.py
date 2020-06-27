# t = int(input())

# for i in range(t):

#     n = int(input())

#     numList = list(int(num) for num in input().split())

#     minValue = min(numList)

#     sumTotal = sum(numList)

#     print(sumTotal - n * minValue)

def solution(elements, n):
    return sum(elements) - n * min(elements)


tc = int(input())
while tc > 0:
    n = int(input())
    elements = list(map(int, input().split()))
    print(solution(elements, n))
    tc -= 1