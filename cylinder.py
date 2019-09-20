#finds area cylinder
#finds volume of cylinder
radius = int(input("Please enter radius of cylinder:"))
height = int(input("Please enter height of cylinder:"))
pie = 3.14159
radius2 = radius * radius
area = 2 * (radius * height * pie) + 2 * (radius2 * pie)
volume = pie * radius2 * height
print("The voulume is:", volume)
print("The area is:" , area)
input("\n\nPress the enter key to exit")
