class Movie:
    def __init__(self, name: str, genre: str, showtime: str):
        self.name = name
        self.genre = genre
        self.showtime = showtime


class Seat():
    def __init__(self):
        self.is_booked = False


class Theatre():
    def __init__(self, seatCount: int):
        self.movies = []
        self.seats = [Seat() for i in range(seatCount)]

    def add_showtime(self, movie):
        self.movies.append(movie)

    def get_remainig_seat(self):
        count = 0

        for seat in self.seats:
            if not seat.is_booked:
                count += 1

        return count
