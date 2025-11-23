
class Item:
    def __init__(self, name_temp: str, weight_temp: int):
        self.names = name_temp
        self.weights = weight_temp

    def __str__(self):
        return f"{self.names} ({self.weights} kg)"

    def name(self):
        return self.names

    def weight(self):
        return self.weights


