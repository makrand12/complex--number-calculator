# --------------
import pandas as pd
import numpy as np
import math

class complex_numbers(object):
    def __init__(self, real=0.00, imag=0.00):
        self.real = real
        self.imag = imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return complex_numbers(real,imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return complex_numbers(real,imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return complex_numbers(real,imag)
    
    def __truediv__(self, other):
        sr, si, o_r, oi = self.real, self.imag,other.real, other.imag # short forms
        r = float(o_r**2 + oi**2)
        return complex_numbers((sr*o_r+si*oi)/r, (si*o_r-sr*oi)/r)

    def absolute(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def conjugate(self):   
        real = self.real
        imag = -self.imag
        return complex_numbers(real,imag)
    
        
    def argument(self):   
        return math.degrees((math.atan(self.imag/self.real)))
    
comp_1 = complex_numbers(3,5)
print('Complex Number 1: ',comp_1)

comp_2 = complex_numbers(4,4)
print('Complex Number 2: ',comp_2)

comp_sum= (comp_1+comp_2)
print('Sum of Complex Number 1 & 2: ', comp_sum)

comp_diff= (comp_1-comp_2)
print('Difference of Complex Number 1 & 2: ',comp_diff)

comp_prod= (comp_1*comp_2)
print('Product of Complex Number 1 & 2: ',comp_prod)

comp_quot= (comp_1/comp_2)
print('Quotient of Complex Number 1 & 2: ',comp_quot)

comp_abs=comp_1.absolute()
print('Absolute value of Complex Number 1: ',comp_abs)

comp_conj= comp_1.conjugate()
print('Conjugate value of Complex Number 1: ',comp_conj)

comp_arg=comp_1.argument()
print('Argument value of Complex Number 1: ',comp_arg) 
    


