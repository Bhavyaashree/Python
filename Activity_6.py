#Task 1: Simulate Bookings Using While Loop

#Write the Program

total_seats = 5

while total_seats > 0:
    print("Seat Booked Successfully")
    print("Remaining Seats:", total_seats - 1)
    total_seats -= 1

print("All Seats Are Filled")


#Task 2: Use For Loop and Range() to Check Seat Numbers

#Write the Program

print("Available Seat Numbers:")

for seat in range (1,11):
    print("Seat Number:", seat)


#Task 3: Stop Booking When Seats Become Full

#Write the Program


total_seats = 5

for booking in range (1,10):

    if booking > total_seats:
        print("No Seats Available")
        break

    if booking == 3:
        print("Checking Special Reservation")
        continue

    pass

    print("Seat", booking, "Booked Successfully")
