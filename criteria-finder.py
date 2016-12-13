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

    return Musician(name, gender, bands, genres, instruments)


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

x = musician_creator()

show_musician(x)
