

class Series:
    count = 0
    average = 0

    def __init__(self, name: str, amount: int, genre: list, rating: int = 0, ):
        self.name = name
        self.amount = str(amount)
        self.genre = genre
        self.total_rating = rating



    def __str__(self):

        return f'''name:{self.name} ({self.amount} seasons)
genres: {self.genre}
rating: {self.count}, average: {self.average} points
        '''

    def rate(self, rate: int = 0):

        if rate < 0 or rate > 6:
            raise ValueError('rating must be between 0 and 5')
        else:
            self.total_rating += rate
            self.count += 1
            self.average = self.total_rating / self.count
            return f"{self.count} rating, average {self.average} points"

def minimum_grade(rating: float, series_lists: list):
    holding_good_rated_shows = []
    for separate_series in series_lists:
        if rating < separate_series.average:
            holding_good_rated_shows.append(separate_series)

    return holding_good_rated_shows

def includes_genre(genre: str, series_lists: list):
    for series_item in series_lists:
        if genre in series_item.genre:
            print(series_item)









# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)
# print(dexter)

series_one = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
series_one.rate(5)

series_four = Series("PowerPuff Girls", 17, ["Crime", "Action", "Cartoon", "Adventure"])
series_four.rate(5)

series_two = Series("South Park", 24, ["Animation", "Comedy"])
series_two.rate(3)

series_three = Series("Friends", 10, ["Romance", "Comedy"])
series_three.rate(2)

series_list = [series_one, series_two, series_three, series_four]


# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)
#
# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)

# includes_genre("Comedy", series_list)
calling_the_minimum_grade = minimum_grade(4.5, series_list)
print(calling_the_minimum_grade[1])