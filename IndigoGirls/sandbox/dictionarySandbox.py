"""
    File created September 20, 2017

    @Author: James Malloy

    This file is used as a test ground for experimenting with dictionaries
"""

test = {"Salad": "Healthy", "Icecream": "Not Healthy"}

print(test.get("Icecream"))
print(test.get("Salad"))
print(test.get("NonExistent"))

test.update({"Added": 5})

print(test.get("Added"))

print("Salad" in test)
