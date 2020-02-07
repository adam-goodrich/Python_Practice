class band:

    number_of_bands = 0

    def __init__(self, genre="", band_name="", albums_released=0):
        band.number_of_bands += 1
        self.genre = genre
        self.band_name = band_name
        self.albums_released = albums_released

    def print_stats(self):
        if self.genre == "":
            print("I do not understand that genre")
        else:
            print(f"The {self.genre} band {self.band_name} has {self.albums_released} albums.")

my_band = band(band_name="Queen", albums_released=15)

my_band.print_stats()