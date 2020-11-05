class Passenger:
    name: str
    email: str
    address: str
    regNo: str
    def __init__(self, name, email, address, regNo):
        self.name = name
        self.email = email
        self.address = address
        self.regNo = regNo

    def __str__(self):
        description = f"{self.name}'s id is {self.regNo} and email is {self.email} and address is {self.address}"
        return description
