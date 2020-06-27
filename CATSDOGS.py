# for t in range(int(input())):
#     c,d,l = map(int,input().split())
#     if l%4!=0:
#         print("no")
#     else:
#         if c>(2*d):
#             min = 4*c - 4*d
#             max = 4*c + 4*d
#             if l<min or l>max:
#                 print("no")
#             else:
#                 print("yes")
#         else:
#             min = 4*d
#             max = 4*d + 4*c
#             if l<min or l>max:
#                 print("no")
#             else:
#                 print("yes")

def solution(cat, dog, legs):
    if legs % 4 != 0:
        return "no"
    elif cat > 2 * dog:
        return "no" if legs < (4 * cat - 4 * dog) or legs > (4 * cat + 4 * dog) else "yes"
    return "no" if legs < (4 * dog) or legs > (4 * dog + 4 * cat) else "yes"

tc = int(input())
while tc > 0:
    cat, dog, legs = map(int, input().split())
    print(solution(cat, dog, legs))
    tc -= 1

