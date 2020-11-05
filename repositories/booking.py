class Booking:
    passenger: str
    flight: str
    ticktype: str
    tickclass: str
    regNo: str

    def __init__(self, passenger, flightNo, ticktype, tickclass, regNo):
        self.passenger = passenger
        self.flightNo = flightNo
        self.ticktype = ticktype
        self.tickclass = tickclass
        self.regNo = regNo