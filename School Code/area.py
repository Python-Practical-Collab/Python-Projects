# Area

"""
    How it works?
    We have created separate functions for each shape and each function takes parameters depening upon what shape it represnts.
    
    eg: for calculating the area of square, we only need its side
        but for rectangle we need its length and width

    Inside each function we are returning the area of that shape, which we are calculating by putting the values in the formula.
    Furthermore, we have used f-strings to generate a proper response.
"""

def square(side: float):
    return f"Area of the square is {side**2}"

def rectangle(length: float, width: float):
    return f"Area of the rectangle is {length*width}"

def circle(radius: float):
    return f"Area of the circle is {3.14 * radius**2}"

def triangle(width: float, height: float):
    return f"Area of the triangle is {1/2 * width * height}"

print(triangle(1, 2))