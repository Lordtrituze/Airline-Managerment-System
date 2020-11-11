from repositories.flight import Flight
from services.aircraftmanager import AircraftManager
import os.path


class FlightManager:
    flight = []
    flightNo = 0

    def __init__(self, aircraft):
        self.aircraft: AircraftManager = aircraft

    def createFlight(self, aircraft, takeoffloc, destination, date, time):
        if aircraft == "" or aircraft == None:
            print("Aircraft can't be empty")
            return  aircraft
        elif takeoffloc == "" or takeoffloc == None:
            print("Take-Off Location can't be empty")
            return  takeoffloc
        elif destination == "" or destination == None:
            print("Destination can't be empty")
            return destination
        elif date == "" or date == None:
            print("Date can't be empty")
            return  date
        elif time == "" or time == None:
            print("Time can't be empty")
            return time
        else:
            pass
        a = self.aircraft.search(aircraft)
        if a:
            self.flightNo += 1
            f = Flight(aircraft, takeoffloc, destination, date, time, self.flightNo)
            strf = f'{f.aircraft:<10}\t{f.takeoffloc:<10}\t{f.destination:<10}\t{f.date:<10}\t{f.time:<10}\t{f.flightNo:<10}\n'
            if os.path.isfile("../files/flights.txt"):
                flightfile = open("../files/flights.txt", "a")
                flightfile.write(strf)
                flightfile.close()
            else:
                flightfile = open("../files/flights.txt", "w")
                flightfile.write(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}\n')
                flightfile.write(strf)
                flightfile.close()
            self.flight.append(f)
        else:
            print('No record for the given aircraft')

    def show(self, f):
        print(f'{f.aircraft:<10}\t{f.takeoffloc:<10}\t{f.destination:<10}\t{f.date:<10}\t{f.time:<10}\t{f.flightNo:<10}')

    def printAll(self):
        print(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}')
        for f in self.flight:
            self.show(f)


    def search(self, flightNo):
        try:
            for f in self.flight:
                if f.flightNo == int(flightNo):
                    print(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}')
                    self.show(f)
                    return f
            else:
                print('There is no Flight with the Flight Number you entered')
        except ValueError:
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


