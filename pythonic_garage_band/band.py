class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

# "Drummer instance. Name = Sheila E."
class Musician:
    pass


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return ""

class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return ""

class Drummer(Musician):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return ""