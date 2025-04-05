import math


def ex01():
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))

    area = 0.5 * b * h

    print(f"The area of the triangle is: {area}")

def ex02():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    perimeter = a + b + c

    print(f"The perimeter of the triangle is: {perimeter}")

def ex03():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))

    perimeter = 2*(l + w)

    print(f"The perimeter of the rectangle is: {perimeter}")

def ex04():
    r = float(input("Enter the radius: "))

    area = math.pi * math.pow(r,2)
    circumference  = 2 * math.pi * r

    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")

def ex05():
    slope = 2
    y_intercept = -2
    x_intercept = (0 - y_intercept) / slope

    print(f"Slope (m): {slope}")
    print(f"Y-intercept: (0, {y_intercept})")
    print(f"X-intercept: ({x_intercept}, 0)")

def ex06():
    import math

    x1, y1 = 2, 2
    x2, y2 = 6, 10

    slope = (y2 - y1) / (x2 - x1)

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"Slope (m) between the points ({x1}, {y1}) and ({x2}, {y2}): {slope}")
    print(f"Euclidean distance between the points: {distance}")

def ex08():
    def calculate_y(x):
        return x ** 2 + 6 * x + 9

    for x in range(-20, 21):
        y = calculate_y(x)
        print(f"x = {x}, y = {y}")
        if y == 0:
            print(f"==> y = 0 when x = {x}")

def ex09():
    word1 = "python"
    word2 = "dragon"

    length1 = len(word1)
    length2 = len(word2)

    print(f"Length of '{word1}' is {length1}")
    print(f"Length of '{word2}' is {length2}")

    comparison = length1 == length2
    print(f"Are lengths equal? {comparison}")

def ex15():
    h = float(input("Enter hour: "))
    r = float(input("Enter rate per hour: "))

    p = r * h
    print("Pay of the person = ", p)

def ex16():
    y = float(input("Enter years: "))

    s = 360 * 365 * y
    print("Seconds of life: ",s)

if __name__ == '__main__':
    ex16()

