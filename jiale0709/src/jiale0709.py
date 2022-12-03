''' Info, Version, Index, Formula, Help '''
def info():
    print("This is Jia Le's Python Library")
    print('This Library is Developed by Jia Le')
    print('Github : JiaLe0709, JiaLeLab')
    
def version():
    print('Jia Le Version : v0.0.8') 
    print('Release Date : 12/4/2022')

def index():
    print("\u0332".join("Index-Note"))
    print("\u0332".join("Index-Basic Math"))
    print('\n- add / plus \n- substract / minus \n- multiply / times \n- divide \n- discount \n- multiplication \n- division \n')
    print("\u0332".join("Index-Polygon & 3-Dimension"))   
    print('\n- interior \n- exterior \n- circumference2 / circumference 3 (2 for 22/7 , 3 for 3.14)')
    print("\u0332".join("Common-Life Math"))   
    print('\n- bmi \n- mm_cm, mm_m, mm_km \n- cm_mm, cm_m, cm_km \n- km_m, km_cm, km_mm')
    
def formula():
    print("\u0332".join("Formula"))    
    print('\n Sum of Interior Angles ((n-2) x 180°) \n Sum of Exterior Angles (360 ÷ numbers of side) \n Circumference (2πr) \n BMI (weight(kg) ÷ (height(m) ** 2))')
    print(" Millimetre to Centimeter (Divide the length value by 10) \n Millimetre to Meter (Divide the length value by 1000) \n Millimetre to Kilometer (Divide the length value by 1e+6)")
    print(' Centimeter to Millimetre (Multiply the length value by 10) \n Centimeter to Meter (Divide the length value by 100) \n Centimeter to Kilometer (Divide the length value by 100000) ')
    print(' Kilometer to Millimetre (Multiply the length value by 1e+6) \n Kilometer to Centimeter (Multiply the length value by 100000) \n Kilometer to Meter (Multiply the length value by 1000)')

def help():
    print("\u0332".join("Help"))
    print("How to use the information data of Jia Le's Library ?")
    print('\nYou can use all of this key to help you: \n info() \n version() \n index() \n formula()')
        

# Math: Add, Plus (+) 
def add(num1, num2):
    print(num1 + num2) 

def plus(num1,num2):    
    print(num1 + num2) 

# Math: Substract, Minus (-)
def substract(num1, num2):
    print(num1 - num2)

def minus(num1, num2):
    print(num1 - num2)

# Math: Multiply, Times (x, *)
def multiply(num1, num2):
    print(num1 * num2)

def times(num1, num2):
    print(num1 * num2)

# Math: Divide (÷, /)
def divide(num1, num2):
    print(num1 / num2)


# Math: Polygon.
# Sum of Interior Angles ((n-2) x 180°)
def interior(n):
    itr_rslt = ((n - 2) * 180)
    print(f'Interior = {itr_rslt}')

# Sum of Exterior Angles (360 ÷ numbers of side)
def exterior(numbers_of_side):
    etr_rslt = (360 / numbers_of_side)
    print(f'Exterior = {etr_rslt}')


# Math: Libraries of Three-dimensional.
# Circumference (2πr) *for 2 & 3 mean (22/7) & (3.14)
def circumference2(radius):
    cir_rslt = (2 * (22/7) * radius)
    print(f'Circumference = {cir_rslt}')

def circumference3(radius):
    cir_rslt = (2 * 3.14 * radius)
    print(f'Circumference = {cir_rslt}')


# Discount System
def discount(price, discount):
    dct_rslt = (price / 100 * discount)
    print(f'Price : {dct_rslt}')


# Math: Multiplication,Division Table
# Multiplication Table
def multiplication(number,Range):
    rng = Range + 1
    for m in range(1,rng):
        print(f'Multiplication Table of {number}')
        print(number,"x",m,'=',(number * m))      

# Division Table
def division(number,Range):
    rng = Range + 1
    for d in range(1,rng):
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


# Coverter of length (mm -cm, m, km | cm - mm,km | km - cm, mm)
# mm - cm, m, km
def mm_cm(mm):
    conv_res =  mm / 10
    print(f'MM to CM = {conv_res} cm')
    
def mm_m(mm):
    conv_res =  mm / 1000
    print(f'MM to M = {conv_res} m')
    
def mm_km(mm):
    conv_res =  mm / 1e+6
    print(f'MM to KM = {conv_res} km')    
    
# cm - mm, m, km    
def cm_mm(cm):
    conv_res = cm * 10
    print(f'CM to MM = {conv_res} mm')
    
def cm_m(cm):
    conv_res = cm / 100
    print(f'CM to M = {conv_res} m')

def cm_km(cm):
    conv_res = cm / 100000
    print(f'CM to KM = {conv_res} km')

# km - mm, cm, m
def km_mm(km):
    conv_res = km * 1000000
    print(f'KM to MM = {conv_res} mm')
    
def km_cm(km):
    conv_res = km * 100000
    print(f'KM to CM = {conv_res} cm')

def km_m(km):
    conv_res = km * 1000
    print(f'KM to M = {conv_res} m')
