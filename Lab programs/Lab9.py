#Define a function which takes TWO objects representing
#complex numbers and returns new complex number with a
#addition of two complex numbers. Define a suitable class
#‘Complex’ to represent the complex number. Develop a
#program to read N (N >=2) complex numbers and to
#compute the addition of N complex numbers. 

class Complex:
    def __init__(self, real=0, imag=0):
		self.real = real
        self.imag = imag
    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
ca = Complex(-2, -5)
cb = Complex(12, 8)
print(ca, '+', cb, '=', (ca + cb))
print('\n',type(ca), id(ca), '\n')
complex_list = []
n = int(input("How many complex numbers you want to add:"))
for i in range(n):
    r = float(input("Enter the real part of the complex number: "))
    im = float(input("Enter the imaginary part of the complex number:"))
    print()
    complex_list.append(Complex(r, im))
sum_series = Complex()
for j in complex_list:
    sum_series += j
print("\nThe sum of the given Complex numbers is:", sum_series)
