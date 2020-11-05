class Booking:
    passenger: str
    flight: str
    ticktype: str
    tickclass: str
    regNo: str

    def __init__(self, passenger, flight, ticktype, tickclass, regNo):
        self.passenger = passenger
        self.flight = flight
        self.ticktype = ticktype
        self.tickclass = tickclass
        self.regNo = regNo