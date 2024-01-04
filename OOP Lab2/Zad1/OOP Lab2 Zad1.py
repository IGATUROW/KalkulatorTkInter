from dog import Dog
from cat import Cat


pies1 = Dog("Burek")
kot1 = Cat("Mruczek")


pies2 = Dog("Azor")
kot2 = Cat("Filemon")

critters = [pies1, kot1, pies2, kot2]


for critter in critters:
    print(critter.sound())