def isPalindrome(s):
    return s == s[::-1]
    
def isValid(s):
    return sorted(set(s)) == [1, 2, 3, 4, 5, 6, 7]
    
tc = int(input())
for _ in range(tc):
    n = int(input())
    elements = list(map(int, input().split()))
    if isPalindrome(elements) and isValid(elements):
        print("yes")
    else:
        print("no")