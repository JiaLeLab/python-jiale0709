''' Info, Version, Index, Formula, Help '''
def info():
    print("This is Jia Le's Python Library")
    print('This Library is Developed by Jia Le')
    print('Github : JiaLe0709, JiaLeLab')
    
def version():
    print('Jia Le Version : v0.0.7') 
    print('Release Date : 12/3/2022')

def index():
    print("\u0332".join("Index-Note"))
    print('You can add p before the data [ Example: padd(5,5) ]to straight away get the result whithout print. Except Example: \n- multiplication \n- division')
    print("\u0332".join("Index-Basic Math"))
    print('\n- add / plus \n- substract / minus \n- multiply / times \n- divide \n- discount \n- multiplication \n- division \n')
    print("\u0332".join("Index-Polygon & 3-Dimension"))   
    print('\n- interior \n- exterior \n- circumference2 / circumference 3 (2 for 22/7 , 3 for 3.14)')
    print("\u0332".join("Common-Life Math"))   
    print('\n- bmi')
    
def formula():
    print("\u0332".join("Formula"))    
    print('\n Sum of Interior Angles ((n-2) x 180°) \n Sum of Exterior Angles (360 ÷ numbers of side) \n Circumference (2πr) \n BMI (weight(kg) ÷ (height(m) ** 2))')

def help():
    print("\u0332".join("Help"))
    print("How to use the information data of Jia Le's Library ?")
    print('\nYou can use all of this key to help you: \n info() \n version() \n index() \n formula()')
        
'''
Basic Math Libraries.
Only work when using Print (for in-case of join another data)
'''
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

''' Can run in without Print (It will straight away print out the output when running the code, You Don't need use "print" but you only can using p+[data]) '''

# Math: Add, Plus (+) 
def padd(num1, num2):
    print(num1 + num2) 

def pplus(num1,num2):    
    print(num1 + num2) 

# Math: Substract, Minus (-)
def psubstract(num1, num2):
    print(num1 - num2)

def pminus(num1, num2):
    print(num1 - num2)

# Math: Multiply, Times (x, *)
def pmultiply(num1, num2):
    print(num1 * num2)

def ptimes(num1, num2):
    print(num1 * num2)

# Math: Divide (÷, /)
def pdivide(num1, num2):
    print(num1 / num2)

''' Libraries of Polygon. '''
# Sum of Interior Angles ((n-2) x 180°)
def interior(n):
    return ((n - 2) * 180)

# Sum of Exterior Angles (360 ÷ numbers of side)
def exterior(numbers_of_side):
    return (360 / numbers_of_side)

''' Can run in without Print (It will straight away print out the output when running the code, You Don't need use "print" but you only can using p+[data]) '''
# Sum of Interior Angles ((n-2) x 180°)
def pinterior(n):
    print((n - 2) * 180)

# Sum of Exterior Angles (360 ÷ numbers of side)
def pexterior(numbers_of_side):
    print(360 / numbers_of_side)

''' Libraries of Three-dimensional. '''
# Math: Circumference (2πr) *for 2 & 3 mean (22/7) & (3.14)
def circumference2(radius):
    return (2 * (22/7) * radius)

def circumference3(radius):
    return (2 * 3.14 * radius)

''' Can run in without Print (It will straight away print out the output when running the code, You Don't need use "print" but you only can using p+[data]) '''
# Math: Circumference (2πr) *for 2 & 3 mean (22/7) & (3.14)
def pcircumference2(radius):
    return (2 * (22/7) * radius)

def pcircumference3(radius):
    return (2 * 3.14 * radius)

''' Counting System '''
# Discount System
def discount(price, discount):
    return (price / 100 * discount)

''' Can run in without Print (It will straight away print out the output when running the code, You Don't need use "print" but you only can using p+[data]) '''
# Discount System
def pdiscount(price, discount):
    print(price / 100 * discount)

# Math: Multiplication,Division Table
'''(12 lines only & Cannot using print.)'''
# Multiplication Table
def multiplication(number):
    for m in range(1,13):
        print(number,"x",m,'=',(number * m))

# Division Table
def division(number):
    for d in range(1,13):
        print(number,"÷",d,'=',(number / d))

# BMi Calculator (BMI = weight ÷ height ^2),(weight / height**2)
def bmi(weight,height):
    # Using rbmi as Result of BMI
    rbmi = weight / (height ** 2)
    print('BMI : ',rbmi)
    # BMI Result
    # (<18.5 is Underweight)
    if rbmi <= 18.5:
        print('You are Underweight.')
    # (> 18.5 – 24.9 is Normal weight)
    elif rbmi > 18.5 and rbmi < 25:
        print('Your are in Normal weight.')
    # (> 25 - 29.9 is Overweight)
    elif rbmi >= 25 and rbmi < 30:
        print('You are Overweight.')
    # (> 30 is Obesity)
    else:
        print('You are Obesity.')
