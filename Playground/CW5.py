class Fraction:
    def __init__(self,numerator = 1, denominator= 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self,other):     
        numerator = 1
        denominator = 1
        if(self.denominator == other.denominator):
            numerator = self.numerator + other.numerator
            denominator = self.denominator
            
        else:
            numerator = self.numerator*other.denominator + other.numerator*self.denominator
            denominator = self.denominator * other.denominator

        tempFraction = Fraction(numerator,denominator) 
        tempFraction.reduce()
        return f'{tempFraction.numerator}/{tempFraction.denominator}'
            
    def __sub__(self,other):     
        numerator = 1
        denominator = 1
        if(self.denominator == other.denominator):
            numerator = self.numerator - other.numerator
            denominator = self.denominator
        else:
            numerator = self.numerator*other.denominator - other.numerator*self.denominator
            denominator = self.denominator * other.denominator

        tempFraction = Fraction(numerator,denominator) 
        tempFraction.reduce()
        return f'{tempFraction.numerator}/{tempFraction.denominator}'   
    
    def __mul__(self,other):     
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        tempFraction = Fraction(numerator,denominator) 
        tempFraction.reduce()
        return f'{tempFraction.numerator}/{tempFraction.denominator}' 

    def __truediv__(self,other):     
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        tempFraction = Fraction(numerator,denominator) 
        tempFraction.reduce()
        return f'{tempFraction.numerator}/{tempFraction.denominator}'

    def __str__(self):
        self.reduce()
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        gcdValue = self.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator/gcdValue
        self.denominator = self.denominator/gcdValue
        # return f'{self.numerator/gcdValue}/{self.denominator/gcdValue}'


    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    @classmethod
    def fromString(cls,fractionInString):
        fractionInString = float(fractionInString)
        numerator = fractionInString * 10000000000000
        denominator = 10000000000000
        return cls(numerator,denominator)




f1 = Fraction(1,2)
f2 = Fraction(3,7)
f3 = Fraction.fromString("2.25")


print(f'f1 is {f1}')
print(f'f2 is {f2}')
print(f'f3 is {f3}')

print()

print(f'f1 + f2 is {f1 + f2}')
print(f'f1 - f2 is {f1 - f2}')
print(f'f1 * f2 is {f1 * f2}')
print(f'f1 / f2 is {f1 / f2}')
print(f'f3 * f2 is {f3 * f2}')

# OUTPUT

# f1 is 1.0/2.0
# f2 is 3.0/7.0
# f3 is 9.0/4.0

# f1 + f2 is 13.0/14.0
# f1 - f2 is 1.0/14.0
# f1 * f2 f2 is 3.0/14.0
# f1 / f2 f2 is 7.0/6.0
# f3 * f2 f2 is 27.0/28.0