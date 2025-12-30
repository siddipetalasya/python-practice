n=int(input())
min=9
while n!=0:
d=n%10
if d<min:
min=d
n=n//10
print(min)