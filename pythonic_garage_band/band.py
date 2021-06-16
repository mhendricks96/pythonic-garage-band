class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        # List comprehension. this iterates through a list and runs a function on each object and makes it easy to save the result in a variable
        solos = [member.play_solo() for member in self.members]
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


        
class Musician:
    def play_solo(self):
        return "play your instrument"

    def get_instrument(self):
        return "instrument"

        
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
        return "face melting guitar solo"


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
        return "bom bom buh bom"


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
        return "rattle boom crash"

   