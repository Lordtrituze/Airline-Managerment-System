from repositories.passenger import Passenger

class PassengerManager():
    passengers = []
    def __init__(self):
        with open("../files/passengers.txt", "rt") as passengerfile:
            next(passengerfile)
            for read in passengerfile.readlines():
                read = read.split()
                # print(read)
                name = read[0]
                email = read[1]
                address = read[2]
                regNo = read[3]
                p = Passenger(name, email, address, regNo)
                self.passengers.append(p)
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
        self.passengers.append(p)
        self.save()
    def show(self, p):
        try:
            print(f'{p.name:<10}\t{p.email:<10}\t{p.address:<10}\t{p.regNo:<10}')
        except ValueError or AttributeError:
            for i in self.passengers:
                if i.regNo == p:
                    self.show(i)

    def printAll(self):
        print(f'{"Name":<10}\t{"Email":<10}\t{"Address":<10}\t{"RegNo":<10}')
        for p in self.passengers:
            self.show(p)


    def search(self, regNo):
        try:
            for p in self.passengers:
                if p.regNo == regNo or p.name == regNo:
                    # self.show(p)
                    return p
            else:
                print('There is no Passenger with the Registration Number you entered')
        except ValueError:
            print('There is no Passenger with the Registration Number you entered')

    def update(self, name, email, address, regNo):
        try:
            p = self.search(regNo)
            p.name = name
            p.email = email
            p.address = address
            print("UPDATED!")
            self.show(p)
        except ValueError or AttributeError:
            return

    def delete(self, regNo):
        try:
            p = self.search(regNo)
            self.passengers.remove(p)
            print("DELETED!")
        except ValueError:
            print('There is no Passenger with the Registration Number you entered')

    def save(self):
        with open("../files/passengers.txt", "w+") as passengerfile:
            passengerfile.write(f'{"Name":<10}\t{"Email":<10}\t{"Address":<10}\t{"RegNo":<10}\n')
            for p in self.passengers:
                passengerfile.write(str(p) + "\n")



