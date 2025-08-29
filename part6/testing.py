music_library = {
   "artists": {
       "Radiohead": {
           "genre": ["Alternative Rock", "Art Rock"],
           "formed_year": 1985,
           "members": ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Philip Selway"],
           "albums": {
               "OK Computer": {
                   "release_year": 1997,
                   "label": "Parlophone",
                   "tracks": [
                       {"title": "Airbag", "duration": "4:44", "plays": 512_345_678},
                       {"title": "Paranoid Android", "duration": "6:23", "plays": 983_123_456},
                       {"title": "No Surprises", "duration": "3:48", "plays": 742_678_123}
                   ]
               },
               "In Rainbows": {
                   "release_year": 2007,
                   "label": "XL Recordings",
                   "tracks": [
                       {"title": "15 Step", "duration": "3:57", "plays": 412_678_345},
                       {"title": "Nude", "duration": "4:15", "plays": 621_345_234},
                       {"title": "Reckoner", "duration": "4:50", "plays": 789_456_321}
                   ]
               }
           }
       },
       "Daft Punk": {
           "genre": ["Electronic", "House"],
           "formed_year": 1993,
           "members": ["Thomas Bangalter", "Guy-Manuel de Homem-Christo"],
           "albums": {
               "Discovery": {
                   "release_year": 2001,
                   "label": "Virgin Records",
                   "tracks": [
                       {"title": "One More Time", "duration": "5:20", "plays": 1_234_567_890},
                       {"title": "Digital Love", "duration": "5:01", "plays": 823_456_789},
                       {"title": "Harder, Better, Faster, Stronger", "duration": "3:44", "plays": 1_045_678_234}
                   ]
               },
               "Random Access Memories": {
                   "release_year": 2013,
                   "label": "Columbia",
                   "tracks": [
                       {"title": "Give Life Back to Music", "duration": "4:34", "plays": 345_678_901},
                       {"title": "Get Lucky", "duration": "6:09", "plays": 2_345_678_901},
                       {"title": "Instant Crush", "duration": "5:37", "plays": 456_789_012}
                   ]
               }
           }
       },
       "Gorillaz": {
           "genre": ["Alternative Rock", "Hip Hop", "Trip Hop"],
           "formed_year": 1998,
           "members": ["2-D", "Murdoc Niccals", "Noodle", "Russel Hobbs"],  # fictional lineup
           "albums": {
               "Demon Days": {
                   "release_year": 2005,
                   "label": "Parlophone",
                   "tracks": [
                       {"title": "Feel Good Inc.", "duration": "3:41", "plays": 1_987_654_321},
                       {"title": "DARE", "duration": "4:04", "plays": 654_321_987},
                       {"title": "Kids with Guns", "duration": "3:45", "plays": 345_678_234}
                   ]
               },
               "Plastic Beach": {
                   "release_year": 2010,
                   "label": "Parlophone",
                   "tracks": [
                       {"title": "Stylo", "duration": "4:30", "plays": 543_210_987},
                       {"title": "On Melancholy Hill", "duration": "3:53", "plays": 876_543_210},
                       {"title": "Superfast Jellyfish", "duration": "2:54", "plays": 210_987_654}
                   ]
               }
           }
       }
   }
}

# print(music_library["artists"]["Gorillaz"]["albums"]["Plastic Beach"]["tracks"][2]["title"])


numbers0 = [3,4,5,6]

billy = [6,5,4,3,4,5]

forty_7 = [56,57,67]

slarty_bartfort = [456789,456789,456789,456789,5678]

my_num1 = sum(numbers0)
my_num2 = sum(billy)
my_num3 = sum(slarty_bartfort)
my_num4 = sum(forty_7)