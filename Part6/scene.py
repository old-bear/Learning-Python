#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Thu Sep  3 17:42:24 2015
# File: scene.py
# Description: 

class Actor:
    def line(self): print self.name + ": " + repr(self.message())

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

if __name__ == '__main__':
    s = Scene()
    s.action()
