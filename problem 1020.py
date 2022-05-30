d = int(input())
year = d//365
print(f"{year} ano(s)")
temp = d%365
month = temp//30
print(f"{month} mes(es)")
day = temp%30
print(f"{day} dia(s)")