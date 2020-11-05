from repositories.passenger import Passenger
class PassengerManager():
    passengers = []
    def createPassenger(self, name, email, address, regNo):
        p = Passenger(name, email, address, regNo)
        self.passengers.append(p)
    def show(self, p):
        print(f'{p.name}\t\t{p.email}\t\t{p.address}\t\t\t{p.regNo}')

    def printAll(self):
        print(f'Name\t\tEmail\t\tAddress\t\t\tRegNo')
        for p in self.passengers:
            self.show(p)


    def search(self, regNo):
        try:
            for p in self.passengers:
                if p.regNo == regNo:
                    self.show(p)
                    return p
        except ValueError:
            print('There is no Passenger with the Registration Number you entered')

    def update(self, name, email, address, regNo):
        p = self.search(regNo)
        p.name = name
        p.email = email
        p.address = address
        print("UPDATED!")
        self.show(p)

    def delete(self, regNo):
        try:
            p = self.search(regNo)
            self.passengers.remove(p)
            print("DELETED!")
        except ValueError:
            print('There is no Passenger with the Registration Number you entered')