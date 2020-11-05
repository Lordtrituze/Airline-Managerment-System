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
