from repositories.flight import Flight
from services.aircraftmanager import AircraftManager


class FlightManager:
    flight = []
    flightNo = 0

    def __init__(self, aircraft):
        self.aircraft: AircraftManager = aircraft

    def createFlight(self, aircraft, takeoffloc, destination, date, time):
        a = self.aircraft.search(aircraft)
        if a:
            self.flightNo += 1
            f = Flight(aircraft, takeoffloc, destination, date, time, self.flightNo)
            self.flight.append(f)
        else:
            print('No record for the given aircraft')

    def show(self, f):
        print(f'{f.aircraft}\t\t{f.takeoffloc}\t\t{f.destination}\t\t{f.date}\t\t{f.time}\t\t\t{f.flightNo}')

    def printAll(self):
        print(f'Aircraft\t\tTakeoffloc\t\tDestination\t\tDate\t\tTime\t\t\tFlightNo')
        for f in self.flight:
            self.show(f)


    def search(self, flightNo):
        for f in self.flight:
            if f.flightNo == int(flightNo):
                print(f'Aircraft\t\tTakeoffloc\t\tDestination\t\tDate\t\tTime\t\t\tFlightNo')
                self.show(f)
                return f
        else:
            print('There is no Flight with the Flight Number you entered')

    def update(self, aircraft, takeoffloc, destination, date, time, flightNo):
        f = self.search(flightNo)
        f.aircraft = aircraft
        f.takeoffloc = takeoffloc
        f.destination = destination
        f.date = date
        f.time = time
        print("UPDATED!")
        self.show(f)

    def delete(self, flightNo):
        try:
            f = self.search(flightNo)
            self.flight.remove(f)
            print("DELETED!")
        except ValueError:
            print('There is no Flight with the Registration Number you entered')


