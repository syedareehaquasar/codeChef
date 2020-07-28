def is_readable(word, letters):
    for ch in word:
        if ch not in letters:
            return "No"
    return "Yes"

letters = input()
tc = int(input())
for i in range(tc):
    word = input()
    print(is_readable(word, letters))


#  ques - https://www.codechef.com/WETS0220