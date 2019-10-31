class Table:
    """contain specific number,seat of each table"""
    def __init__(self, number, seats, remaining_seats=100):
        self.number = number
        self.seats = seats
        self.remaining_seats = remaining_seats

class Booking:
    """contains name, status of booking"""
    def __init__(self, name, table, status=True):
        self.name = name
        self.status = status
        self.table = table
        self.booked_number = []
        self.table.remaining_seats -= table.seats
        if self.table.remaining_seats < 0:
            raise ValueError("Out of seat")
        if table.number not in self.booked_number:
            self.booked_number.append(self.table)
    
    def change_name(self, new_name):
        """change customer name"""
        self.name = new_name


class Restaurant:
    """contains all booking queue"""
    def __init__(self, booking):
        self.booking = booking

    def cancel_booking(self):
        """change status of booking"""
        self.booking.status = False
        self.booking.table.remaining_seats += self.booking.table.seats

    def get_table_number(self):
        """get a table number"""
        return self.booking.table.number

    def get_table_seats(self):
        """get a seats of table"""
        return self.booking.table.seats
