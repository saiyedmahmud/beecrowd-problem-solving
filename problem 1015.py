import math
x1, y1 = input().split()
x2, y2 = input().split()

distance = math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
print(f"{distance:.4f}")