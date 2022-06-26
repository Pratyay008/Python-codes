# Create a class C-2d vector and use it to create another class representing a 3-d vector.

class c2dVec():
    def __init__(self,i ,j) :
        self.iCap=i
        self.jCap=j
    def __str__(self):
        return (f"{self.iCap}i + {self.jCap}j")


class c3dVec(c2dVec):
    def __init__(self,i ,j, k) :
        super().__init__(i, j)
        self.kCap=k
    def __str__(self):
        return (f"{self.iCap}i + {self.jCap}j + {self.kCap}k")


v2d=c2dVec(3,7)
v3d=c3dVec(5,8,7)
print("2d vector is : ",v2d)
print("3d vector is : ",v3d)

