#!/usr/bin/env python
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Fri Apr  8 00:47:52 2016

"""A simulation of a scene in a small play
"""

class Actor:
    def line(self): print(self.name + ": " + repr(self.message()))

class Customer(Actor):
    name = 'customer'
    def message(self): return "that's one ex-bird!"

class Clerk(Actor):
    name = 'clerk'
    def message(self): return "no it isn't..."

class Parrot(Actor):
    name = "parrot"
    def message(self): return None

class Scene:
    def __init__(self):
        self.actors = [Customer(), Clerk(), Parrot()]
        
    def action(self):
        for actor in self.actors:
            actor.line()

            
if __name__ == "__main__":
    s = Scene()
    s.action()
