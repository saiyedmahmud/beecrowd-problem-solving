a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)


maior = (a+b+(abs(a-b)))/2
ans = (maior+c+(abs(maior-c)))/2

print(f"{int(ans)} eh o maior")
