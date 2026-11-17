#Task 1: Store Train Data Using Dictionaries

train = {
    "Train_Number" : 12951,
    "Train_Name" : "Mumbai Rajdhani Express",
    "Source" : "Mumbai",
    "Destination" : "Delhi",
    "Available_Seats" : 120
    }

print("Train Information:")
print(train)
print("\nTrain Number:",train["Train_Number"])
print("Train Name:",train["Train_Name"])
print("Source Station:",train["Source"])
print("Destination Station:",train["Destination"])
print("Available Seats:",train["Available_Seats"])


#Task 2: Access and Update Values

#Create a Dictionary

train = {
    "Train_Number" : 12951,
    "Train_Name" : "Mumbai Rajdhani Express",
    "Available_Seats" : 120
    }

#Display Original Dictionary

print(train)

#Access Dictionary Values

print("Train Name:", train["Train_Name"])
print("Availablke Seats:", train["Available_Seats"])

#Update Seat Availability

train["Available_Seats"] = 95
print(train)

#Add New Value Using update()

train.update({"Platform": 4})
print(train)

#Remove Value Using pop()

train.pop("Platform")
print(train)


#Display Updated Dictionary

print("\nUpdated Train Record:")
print(train)
