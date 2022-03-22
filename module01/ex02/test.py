from vector import Vector

print("Column vector of shape 3 * 1")
v1 = Vector([[0.0], [1.0], [2.0]])
print(v1)

print("\nRow vector of shape 1 * 4")
v2 = Vector([1.1, 3.3, 3.3, 7.7])
print(v2)

print("\nColumn vector of shape 5 * 1")
v3 = Vector(5)
print(v3)

print("\nColumn vector of shape 6 * 1")
v4 = Vector((98, 104))
print(v4)

print("\n2.0 times v1")
v = 2.0 * v1
print(v)

print("\nv1 times 3.1415")
v = v1 * 3.1415
print(v)

print("\nv1 divided by 3.1415")
v = v1 / 3.1415
print(v)

print("\nv1 divided by 0")
v = v1 / 0

print("\nv3 . v3")
print(v3.dot(v3))

print("\nv2 . v2")
print(v2.dot(v2))

print("\nv1 Transpose")
print(v1.T())