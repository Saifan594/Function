print("\033c")

def C(r):
    return 2 * 3.14159265359 * r

def A(r):
    return 3.14159265359 * r ** 2

radius = int(input("Enter radius : "))

circumference = C(radius)
area = A(radius)

print(f"Circumference ≈ {circumference}")
print(f"Area ≈ {area}")