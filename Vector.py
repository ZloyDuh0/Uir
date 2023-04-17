class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x_crd = x
        self.y_crd = y
        self.z_crd = z

    def __add__(self, other):
        return Vector(self.x_crd + other.x_crd, self.y_crd + other.y_crd, self.z_crd + other.z_crd)

    def __sub__(self, other):
        return Vector(self.x_crd - other.x_crd, self.y_crd - other.y_crd, self.z_crd - other.z_crd)

    def vec_mul(self, other):
        return Vector(self.y_crd * other.z_crd - self.z_crd * other.y_crd,
                      self.z_crd * other.x_crd - self.x_crd * other.z_crd,
                      self.x_crd * other.y_crd - self.y_crd * other.x_crd)
    def __mul__(self, other:float):
        return Vector(self.x_crd * other, self.y_crd * other, self.z_crd * other)

    def __truediv__(self, other):
        return Vector(self.x_crd / other, self.y_crd / other, self.z_crd / other)
    
    def __abs__(self):
        return Vector(abs(self.x_crd) , abs(self.y_crd) , abs(self.z_crd))
    
    def __iter__(self):
        yield self.x_crd
        yield self.y_crd
        yield self.z_crd
    
    def __str__(self) -> str:
        return f"|{self.x_crd}, {self.y_crd}, {self.z_crd}|"