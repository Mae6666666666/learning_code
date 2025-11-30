

class MagicPotion:
    def __init__(self, potion):
        self.potion = potion

    def add_ingredients(self, ingredient: str, amount: float):
        self.potion.add_ingredient(ingredient)
        self.potion.add_ingredient(amount)

    def print_recipes(self):
        print(self.potion)


class SecretMagicPotion(MagicPotion):
    def __init__(self, password, potion):
        MagicPotion.__init__(self, potion)
        self.password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password != self.password:
            raise Exception("Wrong password")
        else:
            self.add_ingredient(ingredient, amount)

    def print_recipe(self, password: str):
        if password != self.password:
            raise Exception("Wrong password")
        else:
            print(self.potion)



diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")

diminuendo.print_recipe("pocushocus") # WRONG password!