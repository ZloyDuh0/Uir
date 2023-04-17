from Vector import Vector
from Renderer import render_list
from Particle import particle

vec = Vector(1, 2, 3)
print(Vector(1,2,0).vec_mul(Vector(1,3,0)))
print([1,2,3])
print(list(zip(*[[1,2,3],[4,5,6],[7,8,9]])))

render_list(particle(Vector(0,0,0), Vector(3, 6, 15), 1, -1, 0.5, Vector(100, 100, 100)))