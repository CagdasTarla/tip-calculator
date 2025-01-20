print("Welcome to the motherfucking tip calculator")
total = float(input("What is the total bill?\n"))
tip_perc = int(input("What percentage of tip would tou like to give?\n"))
count_people = int(input("How many people will split the bill?\n"))
result = total*((100+tip_perc)/100)/count_people
print(f"Each person should pay {result}.")
input("Press enter to close program.")