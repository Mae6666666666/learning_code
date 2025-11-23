
#
# music_db = {}
#
# with open("bands2.csv") as bands:
#     for components in bands:
#         no_linebreaks = components.replace("\n", "")
#         breaking_up_components = no_linebreaks.split(",")
#         band_id = breaking_up_components[0]
#         band_name = breaking_up_components[1]
#         band_formed_year = breaking_up_components[2]
#         band_origin_country = breaking_up_components[3]
#         print(band_id)
#
#         music_db[band_id] = {"band name": band_name, "year formed": band_formed_year, "band origin" : band_origin_country}
# print(music_db["B0001"] ["band name"])

import pandas as pd

# bands = pd.read_csv("bands.csv")
# albums = pd.read_csv("albums.csv")
# songs = pd.read_csv("songs.csv")
# # print(bands[bands["name"] == "Gorillaz"]) # the complete
# # print(bands.loc[bands["name"] == "Gorillaz", "formed_year"])
# print(bands.loc[bands["name"] == "Gorillaz", "band_id"])
#  gorillaz_band_id = bands.loc[bands["name"] == "Gorillaz", "band_id"][0]
# print(albums.loc[albums["band_id"] == gorillaz_band_id, "album_id"][1])
# gorillaz_plastic_beach_id = albums.loc[albums["band_id"] == gorillaz_band_id, "album_id"][1]
# print(songs.loc[songs["album_id"] == gorillaz_plastic_beach_id, "title"])






class MusicDb:
    bands_file_name = "bands.csv"
    album_file_name = "albums.csv"
    songs_file_name = "songs.csv"


    def load_data(self):
        self.bands = pd.read_csv(self.bands_file_name)
        self.albums = pd.read_csv(self.album_file_name)
        self.songs = pd.read_csv(self.songs_file_name)


    def search_by_band_name(self, band_name):
        gorillaz_record = self.bands[self.bands["name"] == band_name]
        print(gorillaz_record)

    # you make a def function and put self, an argument in it so its not hardcoded what ur looking for
    # then we make variables and include the self. at the start to remind the class it is in that we can use whatever is also in different defines but are still in classe
    # we have to locate whatever we want with .loc and use square brackets to find the name of whar were searching for. use .value at the end with the [0]
    def search_by_album_name(self, album_title):
        band_id = self.albums.loc[self.albums["title"] == album_title, "band_id"].values[0]
        band_record = self.bands.loc[self.bands["band_id"] == band_id]
        print(band_record)

    def search_band_name_by_song_name(self, song_name):
        album_id = self.songs.loc[self.songs["title"] == song_name, "album_id"].values[0]
        band_id = self.albums.loc[self.albums["album_id"] == album_id, "band_id"].values[0]
        band_name = self.bands.loc[self.bands["band_id"] == band_id, "name"].values[0]
        return band_name




my_built_music_db = MusicDb()

my_built_music_db.load_data()
# my_built_music_db.search_by_band_name("Gorillaz")
# my_built_music_db.search_by_album_name("Plastic Beach")
band_name = my_built_music_db.search_band_name_by_song_name("Feel Good Inc")
print(band_name)