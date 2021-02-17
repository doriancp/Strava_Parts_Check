### ASSIGNED VARIABLES ###
chain_models = {"sh_dura_ace":3000,"kmc_dlc11":4000}  # (as example) could be added if substantial difference between models
riding_type = {"road":2500,"commute":4500,"mountain":5000}  # (as example)

total_millage = 0
total_elevation = 0
total_watts = 0
how_clean = ""


### MAIN FUNCTION ###
def distance_travelled():

    distance_travelled = True
    answer = ""
        
    while distance_travelled == True:

        clean_bike()
        ride_details()
        
        print("Your current millage accounting for wear is:",int(total_millage))
        print("Your chain has",int(3000-total_millage),"km remaining.\n")

        
        if total_millage >= chain_models["sh_dura_ace"]:
            print("Inspect your chain for wear.\n")
        
        answer = input("Do you want to add another ride (Y/N)? ").upper()
 
        if answer == "Y":
            distance_travelled = True
        elif answer == "N":
            distance_travelled = False
            print("Goodbye")

   


### RIDE DETAILS ###
def ride_details():
    global total_millage, total_elevation, total_watts
    
    # USER INPUTS
    while True:
        try:
            distance = int(input("Enter your ride in km: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    total_millage += distance
    

    while True:
        try:
            elevation = int(input("Enter your rides elevation in meters: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    total_elevation += elevation

    while True:
        try:
            watts = int(input("Enter your rides average watts: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    total_watts += watts
    
    # FORMULA
    if total_elevation/total_millage >= 10 and total_watts >= 200:
        total_millage = total_millage * 1.06
        
    elif total_elevation/total_millage >= 10:
        total_millage = total_millage * 1.03
        
    elif watts >= 200:
        total_millage = total_millage * 1.03
        
    return total_millage,total_elevation,total_watts


### CLEANING ###
def clean_bike():
    global how_clean
    
    when_clean = ["A - Once a week","B - Once a month","C - Once every 6 months\n"]
    clean_true = False
    
    while clean_true == False:
        print("How often do you clean your bike?\n")

        for cleaning in when_clean:
            print(cleaning)

        how_clean = input().upper()

        if how_clean == "A" or how_clean == "B" or how_clean == "C":
            clean_true = True
        else:
            how_clean = False
            print("Please enter A, B or C.\n")
            
    return how_clean


distance_travelled()





# while True:
#     try:
#         # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
#         age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         #better try again... Return to the start of the loop
#         continue
#     else:
#         #age was successfully parsed!
#         #we're ready to exit the loop.
#         break
# if age >= 18: 
#     print("You are able to vote in the United States!")
# else:
#     print("You are not able to vote in the United States.")
