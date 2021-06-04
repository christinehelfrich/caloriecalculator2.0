"""
Author: Christine Helfrich
Program title: Calorie Calculator
"""
"""
Here I created a python dictionary master list of all of the food items held in my "database" along with calorie counts for each one. 
The keys are the food names, and the values are the calorie numbers
"""

import pandas as pd

file = 'fooddata1.xls'

df = pd.read_excel(file)

names = df["name"]
calories = df["Calories"] 

namelist = []
calorielist = []

for item in names:
    namelist.append(item)

for item in calories:
    calorielist.append(item)

masterlist = {}

for key in namelist:
    for value in calorielist:
        masterlist[key] = value
        calorielist.remove(value)
        break

def writeinstructions():
    # This function will write the initial instructions for the user
    print("\nHello world, today we will be counting the calories that you have consumed today")
    print("Enter the food items you have eaten today, and when you are finished, type 'calculate'.")

# Here are a few global variables defined for the whole program to use
fooditem = None
allfoods = []
count = 0
servings = 0
uniqueconsumed = []

class Calories():
# This class is in charge of keeping track of and adding up calories
    def init(self):
        # Initialation class with variables allfoods, fooditem, and count all to keep track of the calculation
        self.allfoods = []
        self.fooditem = None
        self.count = 0
        self.uniqueconsumed = []

    def calculate(self, count, allfoods, masterlist, uniqueconsumed):
        # This is the main method which caculates calories. It is a double loopgoin through the master list and also the food list checking
        #the food items are correct and then adding them to the total count.
        for key, value in masterlist.items():
            for item in allfoods:
                if key == item:
                    count += value
        # Display output
        self.consumedfoods(allfoods, masterlist, uniqueconsumed)
        print(f'\nYour calorie count today is: {count}')
        print(f'The foods you consumed today are:\n {uniqueconsumed}\n')
        
    def consumedfoods(self, allfoods, masterlist, uniqueconsumed):
        for item in masterlist:
            if item in allfoods and item != "calculate":
                uniqueconsumed.append(item)


class Execute():
    """
    This class is the controller, controlling the flow of the program, and keeping track of things as it does.
    """

    def init(self):
        # Initialation class with variables allfoods, fooditem, and count all to keep track of the calculation during the flow of the game
        self.allfoods = []
        self.fooditem = None
        self.count = 0

    def addservings(self, fooditem, servings):
        # This method adds an extra food item to the list of foods consumed for every serving, as to keep track of servings.
        if servings > 1:
            for i in range(1, servings):
                # Adds to total food item list
                allfoods.append(fooditem)
        else: 
            pass

    def input(self, fooditem):
        # This is the main method which gets input and controls the flow of which it does so inside a while loop

        # Initial input of a food item, as long as the response isn't "calculate"
        while fooditem != "calculate":
            fooditem = input("\nEnter a food item: ")

            # Makes sure the food item is in the "database". Appends to the "allfoods" list if the condition is met
            if fooditem in masterlist.keys():
                allfoods.append(fooditem)

                # Makes sure the food item isn't "calculate", then asks the user for servings of the food item eaten.
                # The self.addservings method is called to populate the list with an appropriate number of servings
                if fooditem != "calculate":
                    servings = int(input("How many servings did you eat? "))
                    self.addservings(fooditem, servings)

            else: 

                # Alternative condition message for if the food item is not in the database
                if fooditem != "calculate":
                    print("Sorry, your food item is not in the database. Try again.")


def main():
    # Main driver method which calls the classes and methods in the program
    writeinstructions()
    calories = Calories()
    execute = Execute()
    execute.input(fooditem)
    calories.calculate(count, allfoods, masterlist, uniqueconsumed)

main()


