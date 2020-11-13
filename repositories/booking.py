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
        description = f"{self.passenger:<10}\t{self.flightNo:<10}\t{self.ticktype:<10}\t{self.tickclass:<10}\t{self.regNo:<10}\t{self.seatNo:<10}"
        return  description