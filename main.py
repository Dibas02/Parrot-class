class Parrot:

    species = 'bird'

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot('Blu', 10)
woo = Parrot('woo', 15)

print("Blue is a ", blu.species)
print("Woo is a ", woo.species)


print("The first parrot's name is", blu.name, 'and its age is', blu.age)
print("The second parrot's name is", woo.name, 'and its age is', woo.age)