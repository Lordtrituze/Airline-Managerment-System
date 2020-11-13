from repositories.flight import Flight
from services.aircraftmanager import AircraftManager



class FlightManager:
    flights = []
    flightNo = 0

    def __init__(self, aircraft):
        self.aircraft: AircraftManager = aircraft
        with open("../files/flights.txt", "rt") as flightfile:
            next(flightfile)
            for read in flightfile.readlines():
                read = read.split()
                # print(read)
                aircraft = read[0]
                takeoffloc = read[1]
                destination = read[2]
                date = read[3]
                time = read[4]
                flightNo = read[5]
                f = Flight(aircraft, takeoffloc, destination, date, time, flightNo)
                self.flights.append(f)

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
            self.flights.append(f)
            self.save()
        else:
            print('No record for the given aircraft')

    def show(self, f):
        try:
            print(f'{f.aircraft:<10}\t{f.takeoffloc:<10}\t{f.destination:<10}\t{f.date:<10}\t{f.time:<10}\t{f.flightNo:<10}')
        except ValueError or AttributeError:
            for i in self.flights:
                if i.regNo == f:
                    self.show(i)

    def printAll(self):
        print(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}')
        for f in self.flights:
            self.show(f)


    def search(self, flightNo):
        try:
            for f in self.flights:
                if f.flightNo == int(flightNo):
                    print(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}')
                    # self.show(f)
                    return f
            else:
                print('There is no Flight with the Flight Number you entered')
        except ValueError:
            print('There is no Flight with the Flight Number you entered')

    def update(self, aircraft, takeoffloc, destination, date, time, flightNo):
        try:
            f = self.search(flightNo)
            f.aircraft = aircraft
            f.takeoffloc = takeoffloc
            f.destination = destination
            f.date = date
            f.time = time
            print("UPDATED!")
            self.show(f)
        except ValueError or AttributeError:
            return

    def delete(self, flightNo):
        try:
            f = self.search(flightNo)
            self.flights.remove(f)
            print("DELETED!")
        except ValueError:
            print('There is no Flight with the Registration Number you entered')

    def save(self):
        with open("../files/flights.txt", "w+") as flightfile:
            flightfile.write(f'{"Aircraft":<10}\t{"Takeoffloc":<10}\t{"Destination":<10}\t{"Date":<10}\t{"Time":<10}\t{"FlightNo":<10}\n')
            for f in self.flights:
                flightfile.write(str(f) + "\n")



