class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def print_point(self):
        print("x=",self.x)
        print("y=",self.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return point(x,y)
    
    def __sub__(self,other):
        x=self.x - other.x
        y=self.y - other.y
        return point(x,y)
    
p1=point(7,3)
p2=point(3,7)

print(p1-p2)