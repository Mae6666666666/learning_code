
class ComputerGame:
    def __init__(self, computer_name: str, company:str, release: int):
        self.computer_name = computer_name
        self.company = company
        self.release = release

class GameWarehouse(ComputerGame):
    def __init__(self, computer_name: str, company:str, release: int):
        super().__init__(computer_name, company, release)

    def list_games(self):
        names_list = []
        company_list = []
        release_list = []
        names_list.append(self.computer_name)
        company_list.append(self.company)
        release_list.append(self.release)

class GameMuseum(GameWarehouse):
    def __init__(self, computer_name: str, company:str, release: int):
        super().__init__(computer_name, company, release)
