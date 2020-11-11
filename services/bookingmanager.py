from repositories.booking import Booking
from services.passengermanager import PassengerManager
from services.flightmanager import  FlightManager
from services.aircraftmanager import AircraftManager
import os.path
class BookingManager():
    bookings = []
    seat = []

    def __init__(self, passenger, flight, aircraft):
        self.passenger: PassengerManager = passenger
        self.flight: FlightManager = flight
        self.aircraft: AircraftManager = aircraft

    def createBooking(self, passenger, flightNo, ticktype, tickclass, regNo):
        if passenger == "" or passenger == None:
            print("Passenger can't be empty")
            return passenger
        elif flightNo == "" or flightNo == None:
            print("Flight Number can't be empty")
            return flightNo
        elif ticktype == "" or ticktype == None:
            print("Ticket Type can't be empty")
            return ticktype
        elif tickclass == "" or tickclass == None:
            print("Ticket Class can't be empty")
            return tickclass
        else:
            pass
        p = self.passenger.search(passenger)
        f = self.flight.search(flightNo)
        flightaircraft = f.aircraft
        aircraft = self.aircraft.search(flightaircraft)
        capacity = int(aircraft.capacity)
        seatNo = len(self.seat)
        if p and f:
            if seatNo == capacity:
                print("Sorry, the Airplane is full")

            else:
                seatNo += 1
            b = Booking(passenger, flightNo, ticktype, tickclass, regNo, seatNo)
            self.seat.append(b.passenger)
            strb = f'{b.passenger:<10}\t{b.flightNo:<10}\t{b.ticktype:<10}\t{b.tickclass:<10}\t{b.regNo:<10}\t{b.seatNo:<10}\n'
            if os.path.isfile("../files/bookings.txt"):
                bookingfile = open("../files/bookings.txt", "a")
                bookingfile.write(strb)
                bookingfile.close()
            else:
                bookingfile = open("../files/bookings.txt", "w")
                bookingfile.write(f'{"Passenger":<10}\t{"FlightNo":<10}\t{"Ticktype":<10}\t{"Tickclass":<10}\t{"RegNo":<10}\t{"SeatNo":<10}\n')
                bookingfile.write(strb)
                bookingfile.close()
            self.bookings.append(b)
        else:
            print("Either the Passenger or Flight you entered does not exist")

    def show(self, b):
        print(f'{b.passenger:<10}\t{b.flightNo:<10}\t{b.ticktype:<10}\t{b.tickclass:<10}\t{b.regNo:<10}\t{b.seatNo:<10}')

    def printAll(self):
        print(f'{"Passenger":<10}\t{"FlightNo":<10}\t{"Ticktype":<10}\t{"Tickclass":<10}\t{"RegNo":<10}\t{"SeatNo":<10}')
        for b in self.bookings:
            self.show(b)

    def search(self, regNo):
        try:
            for b in self.bookings:
                if b.regNo == regNo:
                    self.show(b)
                    return b
            else:
                print('There is no Booking with the Registration Number you entered')
        except ValueError:
            print('There is no Booking with the Registration Number you entered')

    def update(self, passenger, flight, ticktype, tickclass, regNo):
        b = self.search(regNo)
        b.passenger = passenger
        b.flight = flight
        b.ticktype = ticktype
        b.tickclass = tickclass
        print("UPDATED!")
        self.show(b)

    def delete(self, regNo):
        try:
            b = self.search(regNo)
            self.bookings.remove(b)
            print("DELETED!")
        except ValueError:
            print('There is no Booking with the Registration Number you entered')
