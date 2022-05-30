n = int(input())
h = n//3600
temp = n%3600
m = temp//60
s = temp%60
print(f"{h}:{m}:{s}")