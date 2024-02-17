def trapezoid_area(height, base1, base2):
    area = 0.5 * height * (base1 + base2)
    return area

height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))

area = trapezoid_area(height, base1, base2)
print("The area of the trapezoid is:", area)
