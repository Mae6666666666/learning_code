

class SuperHero:
    def __init__(self, _name: str, _location: str):
        self._name = _name
        self._location = _location




class SuperGroup(SuperHero):
    _members = []
    def __init__(self, _name: str, _location: str):
        super().__init__(_name, _location)

    def __str__(self):
        return f'{self._name} {self._location} {self._members}'

    @property
    def get_name(self):
        return self._name

    @property
    def get_location(self):
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(self.get_location, self.get_name)
        print("members:")
        print(self._members)




superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()