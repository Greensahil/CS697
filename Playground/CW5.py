class Fraction:
    def __init__(self,numerator = 1, denominator= 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self,other):     
        # First make sure that the fractions in both objects have been reduced
        self.reduce()
        other.reduce()
        numerator = 1
        denominator = 1
        if(self.denominator == other.denominator):
            numerator = self.numerator + other.numerator
            denominator = self.denominator

            print(self.reduceStat(numerator,denominator))
            


            
        
    
    def __str__(self):
        self.reduce()
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        gcdValue = self.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator/gcdValue
        self.denominator = self.denominator/gcdValue
        # return f'{self.numerator/gcdValue}/{self.denominator/gcdValue}'

    @staticmethod 
    def reduceStat(numerator,demominator):
        gcdValue = self.gcd(self.numerator,self.denominator)
        numerator = self.numerator/gcdValue
        demominator = self.denominator/gcdValue
        return f'{numerator/gcdValue}/{denominator/gcdValue}'

    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    # @classmethod
    # def fromString(cls,fractionInString):



f1 = Fraction(4,3)
f2 = Fraction(2,3)

print(f1 + f2)