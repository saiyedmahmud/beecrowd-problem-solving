name = input()
fixed_salary = float(input())
total_sold = float(input())
total_salary = ((15 / 100) * total_sold) + fixed_salary

print(f"TOTAL = R$ {total_salary:.2f}")
