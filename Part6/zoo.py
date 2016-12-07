#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Fri Apr  8 00:41:50 2016

"""A simulation of animals' words
"""

class Animal:
    def speak(self): print("What do animal speak?!")
    def reply(self): self.speak()

class Mammal(Animal):
    def speak(self): print("What do mammal speak?!")

class Cat(Mammal):
    def speak(self): print("meow")

class Dog(Mammal):
    def speak(self): print("bark")

class Primate(Mammal):
    def speak(self): print("Hello world")

class Hacker(Primate): pass


if __name__ == "__main__":
    zoo = (Animal(), Mammal(), Cat(), Dog(), Primate(), Hacker())
    for animal in zoo:
        print("%s reply: " % animal.__class__.__name__, end='')
        animal.reply()
