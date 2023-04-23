from Vector import Vector
from Field import take_e, take_b

def particle(cord :Vector, vel :Vector, mass :float, charge :int, time_res :float, rend_dist: Vector):
    ret = []
    new_cord = Vector(0, 0, 0)
    while abs(new_cord) < rend_dist:
        force = (take_e(cord) + Vector.vec_mul(vel, take_b(cord))) * charge
        acc = force / mass
        new_cord = cord + vel * time_res + acc * ((time_res ** 2) / 2) 
        ret.append(new_cord)
        vel = vel + acc * time_res
        cord = new_cord
    return tuple(ret)