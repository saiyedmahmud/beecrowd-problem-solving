product_code_1, unit_1, price_1 = input().split()
product_code_2, unit_2, price_2 = input().split()

product_code_1 = int(product_code_1)
unit_1 = int(unit_1)
price_1 = float(price_1)

total_price_1 = unit_1*price_1



product_code_2 = int(product_code_2)
unit_2 = int(unit_2)
price_2 = float(price_2)

total_price_2 = unit_2*price_2

total_pay = total_price_1 + total_price_2

print(f"Valor a pagar: R$ {total_pay:.2f}")x = float(input()):.2f
print(x)