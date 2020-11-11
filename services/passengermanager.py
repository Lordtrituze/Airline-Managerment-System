from repositories.passenger import Passenger
import os.path
class PassengerManager():
    passengers = []
    def createPassenger(self, name, email, address, regNo):
        if name == "" or name == None:
            print("Name can't be empty")
            return name
        elif email == "" or email == None:
            print("Email can't be empty")
            return email
        elif address == "" or address == None:
            print("Address can't be empty")
            return address
        elif regNo == "" or regNo == None:
            print("Registration Number can't be empty")
            return regNo
        else:
            pass
        p = Passenger(name, email, address, regNo)
        strp = f'{p.name}\t\t{p.email}\t\t{p.address}\t\t\t{p.regNo}\n'
        if os.path.isfile("../files/passengers.txt"):
            passengerfile = open("../files/passengers.txt", "a")
            passengerfile.write(strp)
            passengerfile.close()
        else:
            passengerfile = open("../files/passengers.txt", "w")
            passengerfile.write(f'Name\t\tEmail\t\tAddress\t\t\tRegNo\n')
            passengerfile.write(strp)
            passengerfile.close()
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
                if p.regNo == regNo or p.name == regNo:
                    self.show(p)
                    return p
            else:
                print('There is no Passenger with the Registration Number you entered')
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