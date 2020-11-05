from repositories.flight import Flight
class FlightManager:
    flight = []
    
    def createFlight(self, aircraft, takeoffloc, destination, date, time, regNo):
        f = Flight(aircraft, takeoffloc, destination, date, time, regNo)
        self.flight.append(f)
    def show(self, f):
        print(f'{f.aircraft}\t\t{f.takeoffloc}\t\t{f.destination}\t\t{f.date}\t\t{f.time}\t\t\t{f.regNo}')

    def printAll(self):
        print(f'Aircraft\t\tTakeoffloc\t\tDestination\t\tDate\t\tTime\t\t\tRegNo')
        for f in self.flight:
            self.show(f)


    def search(self, regNo):
        try:
            for f in self.flight:
                if f.regNo == regNo:
                    self.show(f)
                    return f
        except ValueError:
            print('There is no Flight with the Registration Number you entered')

    def update(self, aircraft, takeoffloc, destination, date, time, regNo):
        f = self.search(regNo)
        f.aircraft = aircraft
        f.takeoffloc = takeoffloc
        f.destination = destination
        f.date = date
        f.time = time
        print("UPDATED!")
        self.show(f)

    def delete(self, regNo):
        try:
            f = self.search(regNo)
            self.flight.remove(f)
            print("DELETED!")
        except ValueError:
            print('There is no Flight with the Registration Number you entered')