s = input()
i = 0
c = 0
while i < len(s):
    if s[i] in "aeiouAEIOU":
        c += 1
    i += 1
print(c)
