#Task 1: Using AND Operator

#Create variables for passenger details

passenger_age = 25
ticket_confirmed = True

#Apply AND logical operator

if passenger_age >= 18 and ticket_confirmed:
    print("Passenger Eligible for Travel")

#Task 2: Using OR Operator

#Create seat availability variables

confirmed_seat = False
rac_seat = True

#Apply OR logical operator

if confirmed_seat or rac_seat:
    print("Reservation Available")

#Task 3: Using NOT Operator

#Create cancellation status variable

ticket_cancelled = False

#Apply NOT logical operator

if not ticket_cancelled:
    print("Ticket is Active")
    
#Task 4: Apply Reservation Rules for Senior Citizens

#Create passenger details

passenger_age = 65
payment_completed = True

#Apply reservation condition

if passenger_age >= 60 and payment_completed:
    print("Senior Citizen Reservation Approved")
    
#Task 6: Build Ticket Confirmation System

#Create reservation details

available_seats = 5
payment_status = True

#Apply confirmation logic

if available_seats > 0 and payment_status:
    print("Ticket Confirmed Successfully")
else:
    print("Reservation Failed")

#Task 6: Check Passenger Eligibility for Tatkal Booking

#Create Passenger Details

valid_id_proof = True
booking_time_valid = True

#Apply Tatkal booking conditions

if valid_id_proof and booking_time_valid:
    print("Tatkal Booking Allowed")
else:
    print("Tatkal Booking Denied")

#Task 7: Build Final Reservation Rule Validation Module

#Create Reservation Details

passenger_name = "Rahul Sharma"
passenger_age = 30
available_seats = 2
payment_completed = True
ticket_cancelled = False

#Apply final reservation validation

if (
   passenger_age >= 18 and
   available_seats > 0 and
   payment_completed and
   not ticket_cancelled
):
   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Reservation Status : Confirmed")
else:
   print("Reservation Failed")



