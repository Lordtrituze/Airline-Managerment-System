from random import random
from repositories.aircraft import Aircraft
import random

class AircraftManager:
    aircrafts = []

    def __init__(self):
        with open("../files/aircrafts.txt", "rt") as aircraftfile:
            next(aircraftfile)
            for read in aircraftfile.readlines():
                read = read.split()
                # print(read)
                name = read[0]
                model = read[1]
                capacity = read[2]
                regNo = read[3]
                a = Aircraft(name, model, capacity, regNo)
                self.aircrafts.append(a)

    def createCraft(self, name, model, capacity):
        if name == None or name == "":
            print("Name can't be empty, please fill in details correctly!")
            return name
        elif model == None or model == "":
            print("Model can't be empty, please fill in details correctly!")
            return model
        elif capacity != "":
            try:
                capacity = int(capacity)
            except ValueError:
                print("Capacity must be an Integer!")
                return capacity
        elif capacity == "":
            print("Capacity value is not valid, please fill in details correctly!")
            return capacity
        else:
            pass
        str1, str2, str3 = model[:3], capacity, str(random.randint(1, 999))
        regNo = f"{str1}/{str2}/{str3}"
        a = Aircraft(name, model, capacity, regNo)
        self.aircrafts.append(a)
        self.save()

    def show(self, a):
        try:
            print(f'{a.name:<10}\t{a.model:<10}\t{a.capacity:<10}\t{a.regNo:<10}')
        except ValueError or AttributeError:
            for i in self.aircrafts:
                if i.regNo == a:
                    self.show(i)

    def printAll(self):
        print(f'{"Name":<10}\t{"Model":<10}\t{"Capacity":<10}\t{"RegNo":<10}')
        for a in self.aircrafts:
            self.show(a)


    def search(self, regNo):
        try:
            for a in self.aircrafts:
                if a.regNo == regNo or a.name == regNo:
                    # self.show(a)
                    return a
            else:
                print('There is no Aircraft with the Registration Number you entered')
        except ValueError:
            print('There is no Aircraft with the Registration Number you entered')

    def update(self, name, model, capacity, regNo):
        try:
            a = self.search(regNo)
            a.name = name
            a.model = model
            a.capacity = capacity
            print("UPDATED!")
            self.show(a)
        except ValueError or AttributeError:
            return

    def delete(self, regNo):
        try:
            a = self.search(regNo)
            self.aircrafts.remove(a)
            print("DELETED!")
        except ValueError:
            print('There is no Aircraft with the Registration Number you entered')

    def save(self):
        with open("../files/aircrafts.txt", "w+") as aircraftfile:
            aircraftfile.write(f'{"Name":<10}\t{"Model":<10}\t{"Capacity":<10}\t{"RegNo":<10}\n')
            for a in self.aircrafts:
                aircraftfile.write(str(a) + "\n")


