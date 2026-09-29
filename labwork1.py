# Ex1:Calculate the cỉcle radius 
radius = int(input("Enter circle radius? "))

def circle_area (radius):
    area = 3.14 * (radius**2)
    return area
output = circle_area(radius)
print("Circle area =", end=" ")
print(output)


# Ex2: Convert from Celsius to Fahrenheit 
celsius = float(input("Enter the temperature in Celsius? "))

def conversion (celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
output = conversion (celsius)
print(f"{celsius} (C) = {output} (F)")


# Ex3: Prime 
number = int(input("Enter a number? "))

def isPrime(number):
    if number <= 1:
        print(f"{number} is NOT a prime number")
        return

    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT a prime number")
            return
    print(f"{number} is a prime number")
isPrime(number)

# Ex4: Perfect number 
n = int(input("Enter a number? "))

def isPerfect(n):
    if n <= 0:
        print(f"{n} is NOT a perfect number")
        return
    
    sum = 0
    for i in range (1, n):
        if (n % i == 0):
            sum += i
    if sum == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is NOT a perfect number")
isPerfect(n)

  
# Ex5: Favorite color
color = str(input("What is yout favorite color? ").lower())

list = ["blue", "pink", "black", "red"]
if color in list:
    idx = list.index(color)
    print(f"Your color is at {idx} in my list")
else:
    print("Sorry, I could not find your color")


# Ex6: Creating sequence using range()
range1 = list(range(0,7))
print(f"Range 1 = {range1}")

range2 = list(range(1, 11, 3))
print(f"Range 2 = {range2}")

range3 = list(range(5, 0, -1))
print(f"Range 3 = {range3}")

range4 = list(range(6, -3, -2))
print(f"Range 4 = {range4}")


# Ex7: Remove the dollar sign $
s = str("The price of Taylor Swift concert is $100")

def remove_dollar_sign (s):
    return s.replace("$", "") # remove() method is used in a list, not a string
s = remove_dollar_sign(s)
print(s)


# Ex8: List of even items
l = [1, 4, 5 , -1, 10]

def extract_even (l):
    even_list = []
    for i in l:
        if i % 2 == 0:
           even_list.append(i)
    return even_list
even_numbers = extract_even(l)
print(even_numbers)


# Ex 9: Calculate the factorial
num = int(input("Enter a number here: "))

def factorial (num):
    product = 1
    for i in range (1, num + 1):
        product *= i
    return product
number_factorial = factorial(num)
print(f"{num}! = {number_factorial}")


# Ex10: Get out all of divisors of a number 
numéro = int(input("Enter a number here: "))

def divisors (numéro):
    divisors_list = []
    for i in range (1, numéro + 1):
        if numéro % i == 0:
            divisors_list.append(i)
    return divisors_list
list = divisors(numéro)
print(f"List of all divisors of {numéro}: {list}")


# Ex11: Distance between two points
import math
xA = float(input("The value for xA: "))
yA = float(input("The value for yA: "))
xB = float(input("The value for xB: "))
yB = float(input("The value for yB: "))

def calculation (xA, yA, xB, yB):
    function = math.sqrt(((xB - xA)**2) + ((yB - yA)**2))
    return function
distance = calculation(xA, yA, xB, yB)
print(f"The distance between two points: {distance:.2f}")


# Ex12: Pattern with size m x n
m = int(input("Number of m rows: "))
n = int(input("Number of n columns: "))

def pattern (m,n):
    for i in range (m):
        s = "" # for one line
        for j in range (n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                s += "* " 
            else:
                s += " "
        print(s)
