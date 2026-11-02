#Task 1: Build a Basic Ticket Status Checker

#Create variables for passenger and ticket status

passenger_name = "Rahul Sharma"
ticket_status = "Confirmed"

#Use 'if' statement to check ticket status

if ticket_status == "Confirmed":
    print("Ticket is Confirmed")

#Task 2: Apply If...Else Statement for Ticket Verification

#Create a variable for waiting list number

waiting_list = 3

#Use 'if...else' statement for ticket confirmation checking

if waiting_list == 0:
    print("Ticket Confirmed")
else:
    print("Ticket is in Waiting List")

#Task 3: Use Elif Statement for Multiple Ticket Conditions

#Create a variable for ticket category

ticket_status = "RAC"

#Use if, elif, and else statements

if ticket_status == "Confirmed":
    print("Seat Allocated Successfully")
elif ticket_status == "RAC":
    print("Partial Reservation Available")
else:
    print("Ticket id in Waiting List")

#Task 4: Understanding Indentation in Python

#Write a properly indented Python program

age = 65
if age >= 60:
    print("Passenger Eligible for senior Citizen Discount")

#Task 5: Apply Logical Operators in Railway System

#Create passenger age and booking status variables

age = 65
is_ticket_confirmed = True

#Create passenger age and booking status variables

if age >= 60 and is_ticket_confirmed == True:
    print("Passenger eligible for senior Citizen Benefits")

#Task 6: Build Final Railway Ticket Validation System

#Create passenger and payment details

ticket_status = "Confirmed"
payment_status = "Paid"

#Apply combined conditions using logical operators

if ticket_status == "confirmed" and payment_status == "Paid":
    print("Ticket Successfully Booked")
elif ticket_status == "RAC":
    print("Partial Seat Reservation Available")
else:
    print("Booking Pending")

