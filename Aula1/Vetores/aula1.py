#declaração de arrays e operações
import matplotlib as plt
from numpy import array, dot, linalg

u = array([1,4])
v = array([3,6])

print(f"{u + v}")
print(f"{u * v}") # produto elemento vezes elemento

#produto interno

print(f"{u.dot(v)}")

#norma de um vetor

print(f"{linalg.norm(u)}")

#visualização de vetores

plot
