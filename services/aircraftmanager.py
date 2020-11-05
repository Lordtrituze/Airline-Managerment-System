from random import random

from repositories.aircraft import Aircraft
import random

class AircraftManager:
    aircrafts = []

    def createCraft(self, name, model, capacity):
        str1, str2, str3 = model[:3], capacity, str(random.randint(1, 999))
        regNo = f"{str1}/{str2}/{str3}"
        a = Aircraft(name, model, capacity, regNo)
        self.aircrafts.append(a)

    def show(self, a):
        print(f'{a.name}\t\t\t{a.model}\t\t\t{a.capacity}\t\t\t{a.regNo}')

    def printAll(self):
        print(f'Name\t\t\tModel\t\t\tCapacity\t\t\tRegNo')
        for a in self.aircrafts:
            self.show(a)


    def search(self, regNo):
        try:
            for a in self.aircrafts:
                if a.regNo == regNo or a.name == regNo:
                    self.show(a)
                    return a
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
            print('There is no Aircraft with the Registration Number you entered')

    def delete(self, regNo):
        try:
            a = self.search(regNo)
            self.aircrafts.remove(a)
            print("DELETED!")
        except ValueError:
            print('There is no Aircraft with the Registration Number you entered')




