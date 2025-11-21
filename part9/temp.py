class Band:
    def __init__(self,name: str, fav_song:str, numberOfSongs:int) -> None:
        self.name = name
        self.fav_song = fav_song
        self.numberOfSongs = numberOfSongs

    def mostSongs(self, band0: "Band") -> str:
        if band0.numberOfSongs > self.numberOfSongs:
            return band0.name
        else:
            return self.name





linken_park = Band("Linken Park", "cure for the itch", 130)
gorillaz = Band("gorillaz", "doyathing", 40)

# linken_park.mostSongs()
# gorillaz.mostSongs()
winning_name = linken_park.mostSongs(gorillaz)
print(winning_name)