class Flight:
    aircraft: str
    takeoffloc: str
    destination: str
    date: str
    time: str


    def __init__(self, aircraft, takeoffloc, destination, date, time, flightNo):
        self.aircraft = aircraft
        self.takeoffloc = takeoffloc
        self.destination = destination
        self.date = date
        self.time = time
        self.flightNo = flightNo

    def __str__(self):
        description = f"{self.aircraft:<10}\t{self.takeoffloc:<10}\t{self.destination:<10}\t{self.date:<10}\t{self.time:<10}\t{self.flightNo:<10}"
        return  description