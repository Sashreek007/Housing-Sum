def area(a):
    return a**2

print(area(4))


def leap(a):
    if (a%4==0 and a%100 != 0) or a%400==0:
        print("this is a leap year")
    else:
        print("this is not a leap year")

leap(2024)


