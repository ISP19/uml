class Movie:
    def __init__(self, name: str, genre: str, showtime: str):
        self.name = name
        self.genre = genre
        self.showtime = showtime

class Seat():
    """
    to check the seat that is already booked or not
    """
    def __init__(self):
        self.is_booked = False

class Theatre():
    """
    Theatre class
    """
    def __init__(self, seatCount: int):
        """
        to store the information of movies
        """
        self.movies = []
        self.seats = [Seat() for i in range(seatCount)]

    def add_showtime(self, movie):
        """
        append the movies to list
        """
        self.movies.append(movie)

    def get_remainig_seat(self):
        """
        count the seat remaining
        """
        count = 0

        for seat in self.seats:
            if not seat.is_booked:
                count += 1

        return count
