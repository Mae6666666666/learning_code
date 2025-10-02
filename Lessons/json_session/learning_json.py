# this basically lets u use json to look at json stuff
import json

# opening a file in a json file and naming it video_game_data
with open ("data.json") as video_game_data:
    # json.load basically loads the json file that's in the brackets. it follows the same look as a .write thing
    video_games = json.load(video_game_data)
    # yk how to do a print
    for x in video_games:
        print(x["video_games"]["Cuphead"]["average_time_completion"])
        print(x["video_games"]["Undertale"]["average_time_completion"])
        print(x["video_games"]["Bendy And The Ink Machine"]["average_time_completion"])
        print(x["video_games"]["Splatoon"]["average_time_completion"])
        print(x["video_games"]["Roblox"]["average_time_completion"])


