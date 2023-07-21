import math

#Using formula area of square = square of side
def areaSquare(a):
    area = pow(a,2)        
    return area

# Using formula area(rectangle) = length * breadth
def areaRectangle(a, b):
    area = a * b            
    return area

# using herons formula when all three sides are given
def areaTriangleSide(a, b, c):
    s = (a + b + c) / 2        
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area,2)

#Using formula area(triangle) = base * height / 2
def areaTrianglebh(a, b):
    area = (a * b) / 2    
    return round(area,2)

# Using formula area(circle) = πr^2
def areaCircle(r):
    area = (math.pi * r * r);    
    return round(area, 2)

# using formula area(cylinder) = 2πrh + 2πr^2
def surfaceAreaCylinder(r,h):
    area = (2 * math.pi * r * h) + (2 *math.pi * r * r)
    return round(area, 2)

# Using formula perimeter(square) = 4 * Side
def perimeterSquare(a):
    per = 4 * a
    return per

# Using formula perimeter(rectangle) = 2 (l + b)
def perimeterRectangle(a, b):
    per = 2 * ( a + b)    
    return per
def perimeterTriangle(a, b, c):
    per = a + b + c
    return per

# Using formula perimeter(circle) = 2πr
def perimeterCircle(r):
    per = (2 * math.pi * r )        
    return round(per, 2)

#Providing the menu to the user
print("On which geometric shape would you like to operate on?")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Cylinder")
inp = int(input("Enter your choice(1-5) : "))


#Calculating the values as per the geometric shape choice entered
if(inp == 1):
    print("Functions Available\n1.Area\n2.Perimeter\n3.Both Area and Perimeter")
    i = int(input("Enter your choice(1-3): "))
    a = float(input("Enter the side of square: "))
    if(i == 1):
        ret = areaSquare(a)
        print("Area of square with side",a," is ",ret)
    elif(i == 2):
        ret = perimeterSquare(a)
        print("Perimeter of square with side",a," is ",ret)
    elif(i == 3):
        ret = areaSquare(a)
        print("Area of square with side",a," is ",ret)
        ret = perimeterSquare(a)
        print("Perimeter of square with side",a," is ",ret)
    else:
        print("Invalid Choice")
elif(inp == 2):
    print("Functions Available\n1.Area\n2.Perimeter\n3.Both Area and Perimeter")
    i = int(input("Enter your choice(1-3): "))
    a = float(input("Enter the length of rectangle: "))
    b = float(input("Enter the breadth of rectangle: "))
    if(i == 1):
        ret = areaRectangle(a,b)
        print("Area of rectangle with sides",a,",",b," is ",ret)
    elif(i == 2):
        ret = perimeterRectangle(a,b)
        print("Perimeter of rectangle with sides",a,",",b," is ",ret)
    elif(i == 3):
        ret = areaRectangle(a,b)
        print("Area of rectangle with sides",a,",",b," is ",ret)
        ret = perimeterRectangle(a,b)
        print("Perimeter of rectangle with sides",a,",",b," is ",ret)
    else:
        print("Invalid Choice")
elif(inp == 3):
    print("Functions Available\n1.Area\n2.Perimeter\n3.Both Area and Perimeter")
    i = int(input("Enter your choice(1-3): "))
    if(i == 1):
        j = int(input("How do you want to calculate area?\n1.By using base and height\n2.By using all 3 sides:\n "))
        if(j == 1):
            a = float(input("Enter the base of triangle: "))
            b = float(input("Enter the height of triangle: "))
            ret = areaTrianglebh(a, b)
            print("Area of triangle with base:",a,"height:",b," is ",ret)
        elif(j == 2):
         a = float(input("Enter the side 1 of triangle: "))
         b = float(input("Enter the side 2 of triangle: "))
         c = float(input("Enter the side 3 of triangle: "))
         ret = areaTriangleSide(a, b, c)
         print("Area of triangle with sides:",a,",",b,",",c," is ",ret)
    elif(i == 2):
        a = float(input("Enter the side 1 of triangle: "))
        b = float(input("Enter the side 2 of triangle: "))
        c = float(input("Enter the side 3 of triangle: "))
        ret = perimeterTriangle(a, b, c)
        print("Perimeter of triangle with sides:",a,",",b,",",c," is ",ret)
    elif(i == 3):
        a = float(input("Enter the side 1 of triangle: "))
        b = float(input("Enter the side 2 of triangle: "))
        c = float(input("Enter the side 3 of triangle: "))
        ret = areaTriangleSide(a, b, c)
        print("Area of triangle with sides:",a,",",b,",",c," is ",ret)
        ret = perimeterTriangle(a, b, c)
        print("Perimeter of triangle with sides:",a,",",b,",",c," is ",ret)
    else:
        print("Invalid Choice")
elif(inp == 4):
    print("Functions Available\n1.Area\n2.Perimeter\n3.Both Area and Perimeter")
    i = int(input("Enter your choice(1-3): "))
    a = float(input("Enter the radius of circle: "))
    if(i == 1):
        ret = areaCircle(a)
        print("Area of the circle with radius",a," is ",ret)
    elif(i == 2):
        ret = perimeterCircle(a)
        print("Perimeter of the circle with radius",a," is ",ret)
    elif(i == 3):
        ret = areaCircle(a)
        print("Area of the circle with radius",a," is ",ret)
        ret = perimeterCircle(a)
        print("Perimeter of the circle with radius",a," is ",ret)
    else:
        print("Invalid Choice")
elif(inp == 5):
    print("Functions available for cylinder \nSurface Area")
    r = float(input("Enter the radius of cylinder: "))
    h = float(input("Enter the height of cylinder: "))
    ret = surfaceAreaCylinder(r, h)
    print("The surface area of cylinder with radius",r,"and height",h," is ",ret)
else:
    print("Please select correct value")
