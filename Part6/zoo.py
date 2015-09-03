#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Thu Sep  3 17:34:17 2015
# File: zoo.py
# Description: 

class Animal:
    def speak(self): print "What do animal speak?!"
    def reply(self): self.speak()

class Mammal(Animal):
    def speak(self): print "What do mammal speak?!"

class Cat(Mammal):
    def speak(self): print "meow"

class Dog(Mammal):
    def speak(self): print "bark"

class Primate(Mammal):
    def speak(self): print "Hello world"

class Hacker(Primate): pass

if __name__ == '__main__':
    zoo = [Animal(), Mammal(), Cat(), Dog(), Primate(), Hacker()]
    for animal in zoo:
        animal.reply()
