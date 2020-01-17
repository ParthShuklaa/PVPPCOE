"""
list Demo
"""

MyCars = ["Audi","Tesla","BMW"]
#print(MyCars)
def display():
    for car in MyCars:
        print(car)

MyCars.pop()

display()
print("Final List ")

MyCars.insert(1,"Hummer")
display()
