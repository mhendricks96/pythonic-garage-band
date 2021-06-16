class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

# "Guitarist instance. Name = Joan Jett"
class Musician:
    pass

class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass
