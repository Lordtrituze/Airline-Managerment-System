from repositories.booking import Booking
class BookingManager():
    bookings = []

    def createBooking(self, passenger, flight, ticktype, tickclass, regNo):
        b = Booking(passenger, flight, ticktype, tickclass, regNo)
        self.bookings.append(b)

    def show(self, b):
        print(f'{b.passenger}\t\t{b.flight}\t\t{b.ticktype}\t\t\t{b.tickclass}\t\t\t{b.regNo}')

    def printAll(self):
        print(f'Passenger\t\tFlight\t\tTicketType\t\t\tTicketClass\t\t\tRegNo')
        for b in self.bookings:
            self.show(b)

    def search(self, regNo):
        try:
            for b in self.bookings:
                if b.regNo == regNo:
                    self.show(b)
                    return b
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
