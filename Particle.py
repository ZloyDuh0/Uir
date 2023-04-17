from Vector import Vector
from Field import take_e, take_b

def particle(cord :Vector, vel :Vector, mass :float, charge :int, time_res :float, rend_dist: Vector):
    ret = []
    new_cord = Vector(0, 0, 0)
    tm = 0
    while abs(new_cord) < rend_dist:
        tm += 1
        force = charge * (take_e() + Vector.vec_mul(vel, take_b()))
        acc = force / mass
        new_cord = cord + vel * tm + acc * (tm ** 2/2)
        ret.append(new_cord)
        cord = new_cord
        return tuple(ret)