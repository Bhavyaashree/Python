#Task 1: Create Basic Welcome Function

#Define a welcome function

def welcome_message():
   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Welcome to Railway Reservation System")

#Call the function

welcome_message()

#Task 2: Create Passenger Booking Function

#Define booking function with arguments

def book_ticket(passenger_name, train_name):
    print("Passenger Name :", passenger_name)
    print("Train Name :", train_name)
    print("Reservation Status : Confirmed")

#Call the booking function

book_ticket(
    "Rahul Sharma",
    "Rajdhani Express")

#Task 3: Create Fare Calculation Function

#Define fare calculation function

def calculate_fare(ticket_price, passengers):
    total_amount = ticket_price * passengers
    return total_amount

#Call the function

final_fare = calculate_fare(2450, 2)
print("Final Fare :", final_fare)


#Task 4: Create Passenger Verification Function

def verify_passenger(age):
    if age>= 18:
        return "Eligible for Reservation"
    else:
        return "Not Eligible"

#Call the function

result = verify_passenger(25)
print(result)


#Task 5: Build Ticket Generation Function

#Create ticket generation function
def generate_ticket(
   passenger_name,
   train_name,
   seat_number):
   print("===================================")
   print(" Railway Reservation Ticket ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Train Name :", train_name)
   print("Seat Number :", seat_number)


#Call the function

generate_ticket(
   "Priya Singh",
   "Shatabdi Express",
   "B2-21")


#Task 6: Build Final Booking Function

#Create final booking function
def final_booking_system():

   passenger_name = "Rahul Sharma"
   train_name = "Rajdhani Express"
   seat_number = "A1-12"
   ticket_price = 2450

   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Train Name :", train_name)
   print("Seat Number :", seat_number)
   print("Ticket Price :", ticket_price)
   print("Reservation Confirmed")

#Call the function
final_booking_system()


