# STRAVA CHAIN CHECKER

"""
1. {"chain model":manufacturers recommendation}    Y
2. distanced travelled                             Y
3. average amount of watts by user                 Y
4. elevation over a period                         Y
5. type of riding - road, TT, commute, mountain
6. climate of rider
7. frequency of bike clean
8. miles/km converter
9. ft/m converter
10. cost over millage - what is more cost effective
11. reset if chain changed
"""



### IMPORTS ###
import requests
import urllib3
urllib3.disable_warnings()



### STRAVA AUTHORISATION ###

auth_url = "https://www.strava.com/oauth/token"
payload = {
    'client_id': "",
    'client_secret': "",
    'refresh_token': "",
    'grant_type': "refresh_token",
    'f': 'json'
}



### STRAVA ACCESS ###

# Access Token URL:
activites_url = ""
# Send to server:
res = requests.post(auth_url, data=payload, verify=False)
# Access Token:
access_token = res.json()['access_token']
# Authentication:
header = {'Authorization': 'Bearer ' + access_token}
# Parameters:
param = {'per_page': 200, 'page': 1}
# Assign to variable:
my_dataset = requests.get(activites_url, headers=header, params=param).json()

from datetime import datetime



### PRINT STRAVA DATA ###

# COMPLETE DATA #
print(my_dataset[0], end="")

# recent_rides = my_dataset[0]["start_date"]
# print(recent_rides)

# Distance:
distance_strava = int(my_dataset[0]["distance"]/1000)
# print(distance_strava)

# Elevation:
elevation_strava = int(my_dataset[0]["total_elevation_gain"])
# print(elevation_strava)

# Average Watts:
ave_watts_strava = int(my_dataset[0]["average_watts"])
# print(ave_watts_strava)

# Date:
date_strava = my_dataset[0]["start_date"]
# print(date_strava)

# Upload ID:
# upload_id = my_dataset[0]["upload_id"]
upload_id = my_dataset[0]["upload_id"]
# print(upload_id)

# Bikes IDs:
# "" - Specialized
# "" - Old Red

# how_many_activities = len(my_dataset)
# print(how_many_activities)
# Total Activites is limited to 200
    


total_millage = 0
total_elevation = 0
total_watts = 0



### RIDE DETAILS ###
# Editing in progress

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


# ride_details()