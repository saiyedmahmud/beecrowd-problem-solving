n = int(input())
print(n)
note = n//100
temp = n - (note*100)
print(f"{note} nota(s) de R$ 100,00")

note = temp//50
temp = temp - (note*50)
print(f"{note} nota(s) de R$ 50,00")

note = temp//20
temp = temp - (note*20)
print(f"{note} nota(s) de R$ 20,00")

note = temp//10
temp = temp - (note*10)
print(f"{note} nota(s) de R$ 10,00")

note = temp//5
temp = temp - (note*5)
print(f"{note} nota(s) de R$ 5,00")

note = temp//2
temp = temp - (note*2)
print(f"{note} nota(s) de R$ 2,00")

note = temp//1
temp = temp - (note*1)
print(f"{note} nota(s) de R$ 1,00")