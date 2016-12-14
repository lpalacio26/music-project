musicians = {}


class Musician:

    def __init__(self, name, gender, bands, genre, instruments):
        self.name = name
        self.gender = gender
        self.bands = bands
        self.genre = genre
        self.instruments = instruments

    def add_bands(self, bands_list):
        for i in bands_list:
            self.bands.append(i)

    def add_genre(self, genre_list):
        for i in genre_list:
            self.genre.append(i)

    def add_instruments(self, instruments_list):
        for i in instruments_list:
            self.instruments.append(i)


def musician_creator():

    bands = []
    instruments = []
    genres = []

    def add(thing):
        thing_list = []
        while True:
            print('Which %s do you want to add to your profile? Type "stop" if you\'d like to stop adding %s'
                  % (thing, thing))
            new = input()
            if new == "stop":
                break
            else:
                thing_list.append(new)
        return thing_list

    name = input('What is your name?\n> ')
    gender = input('What is your gender?\n> ')

    bands += add('bands')
    instruments += add('instruments')
    genres += add('genres')

    musicians[name] = Musician(name, gender, bands, genres, instruments)


def show_musician(musician):

    print('NAME: ' + musician.name)
    print('GENDER: ' + musician.gender)
    bands = ""
    for i in musician.bands:
        bands += i + ' - '
    print('BANDS: ' + bands)

    instruments = ""
    for i in musician.instruments:
        instruments += i + ' - '
    print('INSTRUMENTS: ' + instruments)

    genres = ""
    for i in musician.genre:
        genres += i + ' - '
    print('GENRES: ' + genres)

Lorenzo = Musician('Lorenzo', 'Male', ['Radiohead'], ['Jazz'], ['Bass'])
musicians['Lorenzo'] = Lorenzo


def criteria_finder(instruments, genre, bands, gender, musician):

        for elem in musician:

            finder = True

            if instruments != "NA":
                for i in instruments:
                        if i not in musician[elem].instruments:
                            finder = False

            if bands != ["NA"]:
                for i in bands:
                        if i not in musician[elem].bands:
                            finder = False

            if genre != ["NA"]:
                for i in genre:
                        if i not in musician[elem].genre:
                            finder = False

            if gender != "NA":
                if gender != musician[elem].gender:
                    finder = False

            if finder:
                show_musician(musicians[elem])


criteria_finder(['Bass'], ['NA'], ['Radiohead'], 'NA', musicians)
