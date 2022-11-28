# Info, Version, Index, Formula
def info():
    print("This is Jia Le's Python Library")
    print('This Library is Developed by Jia Le')
    
def version():
    print('Jia Le Version : v0.0.4') 
    print('Release Date : 11/28/2022')

def index():
    print("\u0332".join("Index"))
    print('\n- add / plus \n- substract / minus \n- multiply / times\n- divide \n- interior \n- exterior')
    print('- circumference2 / circumference 3 (2 for 22/7 , 3 for 3.14)')
    
def formula():
    print("\u0332".join("Formula"))    
    print('\n Sum of Interior Angles ((n-2) x 180°) \n Sum of Exterior Angles (360 ÷ numbers of side) \n Circumference (2πr)')

# Basic Math Libraries.
# Math: Add, Plus (+) 
def add(num1, num2):
    return num1 + num2    

def plus(num1,num2):    
    return num1 + num2  

# Math: Substract, Minus (-)
def substract(num1, num2):
    return num1 - num2

def minus(num1, num2):
    return num1 - num2

# Math: Multiply, Times (x, *)
def multiply(num1, num2):
    return num1 * num2

def times(num1, num2):
    return num1 * num2

# Math: Divide (÷, /)
def divide(num1, num2):
    return num1 / num2

# Libraries of Polygon.
# Sum of Interior Angles ((n-2) x 180°)
def interior(n):
    return ((n - 2) * 180)

# Sum of Exterior Angles (360 ÷ numbers of side)
def exterior(numbers_of_side):
    return (360 / numbers_of_side)

# Libraries of Three-dimensional.
# Math: Circumference (2πr) *for 2 & 3 mean (22/7) & (3.14)

def circumference2(r):
    return (2 * (22/7) * r)

def circumference3(r):
    return (2 * 3.14 * r)
