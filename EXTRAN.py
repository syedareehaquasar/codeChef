# def solve():
#     n=int(input())
#     li=list(map(int,input().split()))
#     li.sort()
#     if(li[1]-li[0]!=1):
#         return li[0]
#     elif(li[-1]-li[-2]!=1):
#         return li[-1]
#     else:
#         for i in range(1,len(li)-1):
#             if(li[i]==li[i+1]):
#                 return li[i]
                
                
# for _ in range(int(input())):
#     print(solve())

def solution(elements, n):
    if elements[1] - elements[0] != 1:
        return elements[0]
    elif elements[-1] - elements[-2] != 1:
        return elements[-1]
    for i in range(1, n - 1):
        if elements[i] == elements[i + 1]:
            return elements[i]

tc = int(input())
while tc > 0:
    n = int(input())
    elements = list(map(int, input().split()))
    print(solution(sorted(elements), n))
    tc -= 1