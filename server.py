import urllib2
from bs4 import BeautifulSoup
from sets import Set

if __name__ == "__main__":
    done = True
    usernames = []
    while done:
        s = raw_input(">")
        if s == "done":
            done = False
        else:
            usernames.append(s)
    data = [urllib2.urlopen("http://myanimelist.net/malappinfo.php?u="+x+"&status=all&type=anime").read() for x in usernames]

    data = [BeautifulSoup(user,"xml").myanimelist for user in data]
    all_data = [Set([]) for x in data]

    index = 0
    for user in data:
        for anime in user:
            if anime.name == "anime":
                all_data[index].add(anime.series_title)
        index += 1


    for line in reduce(lambda x, y: x & y, all_data):
        print line.__str__()[14:-15]
        
