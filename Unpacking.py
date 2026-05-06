data =(10 , 20 ,30)
x,y,z= data
print(data)
print(x,y,z)

#__________________________________________
pairs = [(1,2), (3,4)]
for item in pairs:
    print(item[0], item[1])

    d = {"a": 1, "b": 2}

for key, value in d.items():
    print(key, value)

#----------------------------------------
#यही logic robot navigation में use होता है
def move(x, y):
    print(f"Moving to {x}, {y}")

points = [(10, 20), (30, 40)]

for x, y in points:
    move(x, y)