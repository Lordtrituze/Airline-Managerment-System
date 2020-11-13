class Booking:
    passenger: str
    flight: str
    ticktype: str
    tickclass: str
    regNo: str

    def __init__(self, passenger, flightNo, ticktype, tickclass, regNo, seatNo):
        self.passenger = passenger
        self.flightNo = flightNo
        self.ticktype = ticktype
        self.tickclass = tickclass
        self.regNo = regNo
        self.seatNo = seatNo

    def __str__(self):
        description = f"{self.passenger} {self.flightNo} {self.ticktype} {self.tickclass} {self.regNo} {self.seatNo}"
        return  description