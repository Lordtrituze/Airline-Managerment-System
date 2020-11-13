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
        description = f"{self.name:<10}\t{self.email:<10}\t{self.address:<10}\t{self.regNo:<10}"
        return description
