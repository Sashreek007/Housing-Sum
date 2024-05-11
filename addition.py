def addition(a,b):
    print(a+b)

addition(2,3)
print(5/2)
def dis(price, discount):
    dprice= (discount/100)*price
    return price -dprice
print(dis(1500, 50))


def relation_to_luke(name):
    if name == "Darth Vader":
        return "Luke, I am your father."
    elif name == "Leia":
        return "Luke, I am your sister."
    elif name == "Han":
        return "Luke, I am your brother in law."
    elif name == "R2D2":
        return "Luke, I am your droid."

print(relation_to_luke("Darth Vader"))


def series_resistance(lst):
    sum1 = 0  # Initialize sum1 before using it
    for i in lst:
        sum1 += i
    return '"{} ohms"'.format(sum1)

print(series_resistance([1, 5, 6, 3]))

print(121**0.5)
def circle_or_square(rad, area):
    circumference= 2*3.14*rad
    premi=(area**0.5)*4
    if circumference>premi:
        return True
    else:
        return False
print(circle_or_square(16, 625))

def factorial(num):
    if num ==0:
        return 1
    else:
        fact=1
        for i in range(1,num+1):
            fact *= i
        return fact
 
print(factorial(4))


def factorial(num):
    if num ==0:
        return 1
    else:
        return num*factorial(num-1)
    

def damage(damag,speed,units):
    if damag <0  or speed <0:
        return "invalid"
    elif units == "minute":
        return damag * speed * 60
    elif units == "hour":
        return damag * speed * 3600
    elif units=="second":
        return damag * speed

print(damage(100, 1, "minute"))

def find_even_nums(num):
    val= [i for i in range(1,num) if i % 2 == 0]
    return val

print(find_even_nums(8))

def showdown(p1, p2):
    p1_ind= p1.index("Bang!")
    p2_ind= p2.index("Bang!")
    if p1_ind<p2_ind:
        return "p1"
    elif p2_ind< p1_ind:
        return "p2"
    else:
        return "tie"
print(showdown("   Bang!        ","        Bang!   "))

 


def get_student_names(students):
    values=[]
    for value in students.values():
        values.append(value)
    return sorted(values)

print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))

def return_unique(lst):
    val=[]
    for i in lst:
        if lst.count(i)==1:
            val.append(i)
    return list(val)

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
            

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None 
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        x = (-b + (b**2 -4*a*c)**0.5)/2*a
        return x
	
print(quadratic_equation(1, 2, -3))

