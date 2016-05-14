from anime import Anime


ALL, WATCHING, COMPLETED, ON_HOLD, DROP, PTW = range(0,6)

class Person:
    """
    Stores lists of anime on a person's MAL
    === Attributes ===
    @type watching : List[ anime ]
    @type completed : List[ anime ]
    @type on_hold : List[ anime ]
    @type ptw : List[ anime ]
    @type all : List[ anime ]
    @type status : int
        Determines which list to iterate through
    @type index : int
        Determines where the iterator is
    """
    def __init__(self, list):
        """
        @type list : BeautifulSoup
            The person's anime list converted into beautiful soup
        """
        self.watching = []
        self.completed = []
        self.on_hold = []
        self.drop = []
        self.ptw = []
        self.all = []
        self.statuses = [self.all, self.watching, self.completed, self.on_hold, self.drop, self.ptw]
        self.status = 0
        self.index = 0
        for anime in list:
            if anime.name == "anime":
                if anime.my_status.getText() == "1":
                    self.watching.append(Anime(anime))
                elif anime.my_status.getText() == "2":
                    self.completed.append(Anime(anime))
                elif anime.my_status.getText() == "3":
                    self.on_hold.append(Anime(anime))
                elif anime.my_status.getText() == "4":
                    self.drop.append(Anime(anime))
                elif anime.my_status.getText() == "5":
                    self.ptw.append(Anime(anime))
                self.all.append(Anime(anime))
                
    def set_iter(self, status):
        self.status = status
        return self

    def hasNext(self):
        return self.index != len(self.statuses[self.status])

    def current(self):
        return self.statuses[self.status][self.index]

    def next(self):
        self.index += 1
        return self.statuses[self.status][self.index - 1]
    
