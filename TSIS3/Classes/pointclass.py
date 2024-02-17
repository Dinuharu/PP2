class Pointclass:
    def __init__(self):
        self.x = int(input("Enter x coordinate: "))
        self.y = int(input("Enter y coordinate: "))  

    def show(self):
        print("coordinates : ", self.x, self.y)

    def move(self):
        c = int(input("Enter x coordinate to move to: "))
        v = int(input("Enter y coordinate to move to: "))
        self.x = c
        self.y = v

    def distance(self):
        self.x2 = int(input("Enter x coordinate of the second point: "))
        self.y2 = int(input("Enter y coordinate of the second point: "))
        distance = ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 0.5
        print("Distance between the points:", distance)

z = Pointclass()
z.show()
z.move()
z.show()
z.distance()
z.show()
