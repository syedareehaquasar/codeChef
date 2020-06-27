# t = int(input())
# while t > 0:
#     n, k = map(int, input().split())
#     lst = list(map(int, input().split()))
#     lst.sort()
#     lst1 = []

#     if k >= (n - k):
#         for i in range(n - k):
#             lst1.append(lst[i])
#     else:
#         for i in range(k):
#             lst1.append(lst[i])

#     print(abs((sum(lst) - sum(lst1)) - sum(lst1)))
#     t -= 1

def solution(n, k, elements):
    if k >= (n - k):
        return sum(elements[n - k:]) - sum(elements[:n - k])
    return sum(elements[k:]) - sum(elements[:k])

tc = int(input())
while tc > 0:
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))
    print(solution(n, k, sorted(elements)))
    tc -= 1