#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rujie, Jiang jrjbear@gmail.com
# Date: Thu Sep  3 17:17:29 2015
# File: lunch.py
# Description: 

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self): self.customer.printFood()        

class Customer:
    def __init__(self): self.food = None
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self): print self.food

class Employee:
    def takeOrder(self, foodName): return Food(foodName)

class Food:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

if __name__ == '__main__':
    lunch = Lunch()
    food = 'sandwitch'
    print "Customer orders %s => RESULT:" % food,
    lunch.order(food)
    lunch.result()

    food = 'burritos'
    print "Customer orders %s => RESULT:" % food,
    lunch.order(food)
    lunch.result()        
