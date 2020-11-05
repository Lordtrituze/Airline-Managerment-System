# from AMS import Aircraft1
# import AMSmanager


menuOption = int(input (f"""
    Airline Management Menu
    Enter (1) to Manage Aircrafts
    Enter (2) to Manage Flights
    Enter (3) to Manage Bookings
    Enter (4) to Manage Passengers
    Enter (0) to Exit Menu
    :"""))
if menuOption == 0:
    exit()
elif menuOption == 1:
    menuOption = int(input(f"""
    Aircraft Management Menu
    Enter (1) to Create Aircrafts
    Enter (2) to Search Aircrafts
    Enter (3) to Update Aircrafts
    Enter (4) to Delete Aircrafts
    Enter (5) to Print All Aircrafts
    Enter (0) to Exit Menu
    :"""))
    if menuOption == 1:
        from AMSmanager import AircraftManager
        
        