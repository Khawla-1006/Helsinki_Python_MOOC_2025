class Series :
    def __init__(self, title: str, seasons: int, genre: list):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.rating = 0
        self.r = []
        self.num_of_rating = 0
        self.avg = 0
    

    def rate(self, rating:int):
        self.rating = rating
        self.r.append(self.rating)
        self.num_of_rating = len(self.r)
        self.avg = sum(self.r) / self.num_of_rating

    def __str__(self):
        a = f"{self.title} ({self.seasons} seasons)\n"
        b = f"genres: {", ".join(self.genre)}\n"
        if self.num_of_rating != 0 :
            c = f"{self.num_of_rating} ratings, average {self.avg:.1f} points"
        else :
            c = f"no ratings"
        return a+b+c
    
    def title(self):
        return f"{self.title}"
    

def minimum_grade(rating: float, series_list :list):
    arr = []
    for s in series_list :
        if s.rating >= rating :
            arr.append(s)
    return arr

def includes_genre(genre: str, series_list: list):
    arr2 = []
    for s in series_list :
        for g in s.genre :
            if g == genre :
                arr2.append(s)
    return arr2

    
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)