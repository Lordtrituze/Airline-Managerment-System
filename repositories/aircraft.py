class Aircraft:
    name: str
    model: str
    capacity: int
    regNo: str
    def __init__(self, name, model, capacity, regNo):
        self.name = name
        self.model = model
        self.capacity = capacity
        self.regNo = regNo

    def __str__(self):
        description = f"{self.name:<10}\t{self.model:<10}\t{self.capacity:<10}\t{self.regNo:<10}"
        return  description