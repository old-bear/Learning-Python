#!/usr/bin/env python3
# Author: Rujie Jiang jrjbear@gmail.com
# Date: Fri Apr  8 00:34:14 2016

"""A simulation of lunch ordering procedure
"""

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.placeOrder(food_name, self.employee)

    def result(self): self.customer.printFood()        

    
class Customer:
    def __init__(self): self.food = None
    
    def placeOrder(self, food_name, employee):
        self.food = employee.takeOrder(food_name)

    def printFood(self): print(self.food)

    
class Employee:
    def takeOrder(self, food_name): return Food(food_name)

    
class Food:
    def __init__(self, name): self.name = name
    def __str__(self): return "Food(" + self.name + ")"

    
if __name__ == "__main__":
    lunch = Lunch()
    food = "sandwitch"
    print("Customer orders: %s" % food)
    lunch.order(food)
    print("Check: ", end='')
    lunch.result()

    food = "burritos"
    print("\nCustomer orders: %s" % food)
    lunch.order(food)
    print("Check: ", end='')
    lunch.result()
