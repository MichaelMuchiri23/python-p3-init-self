#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

#Case examples
fido = Dog("Fido", "German shepherd")
print(fido.name)
print(fido.breed)        