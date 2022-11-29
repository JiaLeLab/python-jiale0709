# Info, Version, Index, Formula, Help
def info():
    print("This is Jia Le's Python Library")
    print('This Library is Developed by Jia Le')
    print('Github : JiaLe0709, JiaLeLab')
    
def version():
    print('Jia Le Version : v0.0.5') 
    print('Release Date : 11/29/2022')

def index():
    print("\u0332".join("Index-Basic Math"))
    print('\n- add / plus \n- substract / minus \n- multiply / times \n- divide \n- discount \n- multiplication \n- division \n')
    print("\u0332".join("Index-Polygon & 3-Dimension"))   
    print('\n- interior \n- exterior \n- circumference2 / circumference 3 (2 for 22/7 , 3 for 3.14)')
    
def formula():
    print("\u0332".join("Formula"))    
    print('\n Sum of Interior Angles ((n-2) x 180°) \n Sum of Exterior Angles (360 ÷ numbers of side) \n Circumference (2πr)')

def help():
    print("\u0332".join("Help"))
    print("How to use the information data of Jia Le's Library ?")
    print('\nYou can use :\n info() \n version() \n index() \n formula()')
        
        
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
def circumference2(radius):
    return (2 * (22/7) * radius)

def circumference3(radius):
    return (2 * 3.14 * radius)

# Discount System
def discount(price, discount):
    return (price / 100 * discount)

# Multiplication Table
def multiplication(number):
    for m in range(1,13):
        print(number,"x",m,'=',(number * m))

# Division Table
def division(number):
    for d in range(1,13):
        print(number,"÷",d,'=',(number / d))
