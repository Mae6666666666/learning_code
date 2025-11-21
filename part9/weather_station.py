

class WeatherStation:
    observation_list = []
    def __init__(self, name_temp):
        self.name = name_temp

    def add_observation(self, observation: str):
        self.observation_list.append(observation)

    @property
    def latest_observation(self):
        return self.observation_list[-1]


    def number_of_observations(self):
        observation_length = len(self.observation_list)
        return observation_length

    def __str__(self):
        return f"{self.name}, {len(self.observation_list)} observations"


station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation)

station.add_observation("Thunderstorm")
print(station.latest_observation)

print(station.number_of_observations())
print(station)
