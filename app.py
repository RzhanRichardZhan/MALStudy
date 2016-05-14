import urllib2
from bs4 import BeautifulSoup
from person import Person

ALL, WATCHING, COMPLETED, ON_HOLD, DROP, PTW = range(0,6)

def intersection(people, status):
    iter_list = []
    index = 0
    while index < len(people):
        iter_list.append(people[index].set_iter(status[index]))
        index += 1
        
    all_list = []
    while all(x.hasNext() for x in iter_list):
        if all(x.current() == iter_list[0].current() for x in iter_list):
            anime = iter_list[0].next()
            for person in iter_list[1:]:
                anime.add_score(person.next())
            all_list.append(anime)
        else:
            maximum = max([person.current() for person in iter_list])
            for person in iter_list:
                if person.current() < maximum:
                    person.next()
    for x in all_list:
        print x
        for y in x.scores:
            print y
        
    


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
    persons = [ Person(BeautifulSoup(user, "xml").myanimelist) for user in data]
    print "Finished Souping"
    intersection(persons,[COMPLETED for x in persons])
