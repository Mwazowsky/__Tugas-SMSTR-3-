class BodyMassIndex:
    def __init__(self, name, country, height, weight):
        self.name = name 
        self.country = country
        self.height = height
        self.weight = weight

    def Get_Info(self):
        return "Name : " + self.name + " From " + self.country

    def Get_BMI(self):
        bmi = self.weight / ((self.height ** 2) / 100)
        return bmi * 100

name = str(input("Please enter your nickname : "))
country = str(input("Where are you from ? "))
height = float(input("Enter height : "))
weight = float(input("Enter weight : "))

bmi = BodyMassIndex(name, country, height, weight)
myBMI = bmi.Get_BMI()

print(bmi.Get_Info() + f', Your Body Mass Index is : {myBMI:.2f}')

if myBMI <= 18.50:
    print("Berat Badan anda Kurang")
elif myBMI <= 22.90:
    print("Berat Badan anda Normal")
elif myBMI <= 23.90:
    print("Berat Badan anda Berlebih (Cenderung Obesitas)")
else:
    print("Obesitas")
