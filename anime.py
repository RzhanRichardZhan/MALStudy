class Anime:
    def __init__(self, anime):
        self.id = int(anime.series_animedb_id.__str__()[19:-20])
        self.title = anime.series_title.__str__()[14:-15]
        self.scores = [int(anime.my_score.__str__()[10:-11])]

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def add_score(self, other):
        self.scores.append(other.scores[0])

    def get_id(self):
        return self.id.__str__()
        
    def __str__(self):
        return self.title
