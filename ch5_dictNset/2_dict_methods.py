
marks = {
    "Khari": 100,
    "Shubham": 56, 
    "Rohan": 23,
    0:"Khari"
}

print(marks.items())
print(marks.keys())
marks.update({"Khari":99, "Renuka":45})
print(marks.items())

print(marks.get("Khari")) # prints none
print(marks["Harry"]) # throw error

# pop, pop item

