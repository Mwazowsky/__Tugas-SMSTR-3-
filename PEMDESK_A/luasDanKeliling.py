from math import pi

class Shapes:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def Get_Name(self):
        return self.shape_name

    def CircleArea(self, radian):
        return pi * radian ** 2

    def CircleCircumference(self, radian):
        return 2 * pi * radian
        
    def TriangleArea(self, a, b, c):
        s = (a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

    def TrianglePerimeter(self, a, b, c):
        return a + b + c
    
    def RectangleArea(self, width, length):
        return width * length
    
    def RectangleCircumference(self, width, length):
        return (width * 2) + (length * 2)

    def SquareArea(self, side):
        return side ** 2

    def SquareCircumference(self, side):
        return side * 4


nama = str(input("Bangun mana ? (lingkaran/segitiga/persegi panjang/persegi)")).lower()
nameOfShape = Shapes(nama)

if nameOfShape.Get_Name() == "lingkaran":
    r = float(input("Masukkan jari jari :"))

    print(f'Luas Lingkaran = {nameOfShape.CircleArea(r):.2f} cm')
    print(f'Keliling Lingkaran = {nameOfShape.CircleCircumference(r):.2f} cm')

elif nameOfShape.Get_Name() == "segitiga":
    a = float(input("Masukkan sisi 1 :"))
    b = float(input("Masukkan sisi 2 :"))
    c = float(input("Masukkan sisi 3 :"))

    print(f'Luas Segitiga = {nameOfShape.TriangleArea(a, b, c):.2f} cm')
    print(f'Keliling Segitiga = {nameOfShape.TrianglePerimeter(a, b, c):.2f} cm')

elif nameOfShape.Get_Name() == "persegi panjang":
    width = float(input("Masukkan lebar :"))
    length = float(input("Masukkan Panjang"))

    print(f'Luas Persegi Panjang = {nameOfShape.RectangleArea(width, length):.2f} cm')
    print(f'Keliling Persegi Panjang = {nameOfShape.RectangleCircumference(width, length):.2f} cm')

elif nameOfShape.Get_Name() == "persegi":
    side = float(input("Masukkan sisi :"))

    print(f'Luas Persegi = {nameOfShape.SquareArea(side):.2f} cm')
    print(f'Keliling Persegi = {nameOfShape.SquareCircumference(side):.2f} cm')

else:
    print("Maaf nama Bangun datar yang anda masukkan salah atau tidak ada dalam list")