
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

bands = pd.read_csv("bands.csv")
print(bands["band_id"][0])
