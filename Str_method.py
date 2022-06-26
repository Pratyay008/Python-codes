# Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.


class vec():
    def __init__(self,i,j,k):
        self.iCap=i
        self.jCap=j
        self.kCap=k
    def __str__ (self):
        return (f"The vector is : {self.iCap}i + {self.jCap}j + {self.kCap}k")


vec3d=vec(7,8,10)        
print(vec3d)

