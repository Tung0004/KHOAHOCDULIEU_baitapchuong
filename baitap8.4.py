# Tính diện tích tam giác 
# Công thức hêrong
import math #note: dùng công thức tính toán phải dùng "import math"
print("Nhập số đo ba cạnh của tam giác")
a = eval(input("cạnh a = "))
b = eval(input("cạnh b = "))
c = eval(input("cạnh c = "))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là:",s)