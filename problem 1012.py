a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)
pi = 3.14159

rectangled_triangle =(1/2)*(a*c) 
circel = pi*c**2
trapezium = ((a+b)*c)/2
square = b**2
rectangle = a*b

print(f"TRIANGULO: {rectangled_triangle:.3f}")
print(f"CIRCULO: {circel:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")


