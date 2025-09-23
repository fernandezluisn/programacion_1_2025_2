vector = [9, 5, 8]
print(vector)
print(f"id original de vector {id(vector)}")

vector[2] = 6
print(f"id de vector luego de la modificación {id(vector)}")
print(vector)