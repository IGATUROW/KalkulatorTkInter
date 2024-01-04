import unittest



class Show:
    def __init__(self, title, room, hour, minute, day, month, year):
        self.title = title
        self.room = room
        self.hour = hour
        self.minute = minute
        self.day = day
        self.month = month
        self.year = year
        self.reserved_seats_count = 0

    def reserve(self, seat):
        seat.reserved = True
        self.reserved_seats_count += 1


class ShowSchedule:
    pass


class Customer:
    def __init__(self, login):
        self.login = login



class Room:
    def __init__(self, number, rows, seats_in_row):
        self.number = number
        self.rows = rows
        self.seats_in_row = seats_in_row

class Seat:
    pass


class ShowScheduleShow:
    pass


class CinemaTest(unittest.TestCase):
    def can_reserve_place_in_empty_cinema(self):
        customer = Customer("anonymous")
        room = Room(1, 20, 15)
        seat = Seat(1, 5)
        schedule = ShowSchedule()
        show = Show("Akademia", room, 13, 15, 9, 12, 2023)
        show.reserve(seat)
        self.assertEgual(show.reserved_seats_count, 1)
        self.assertTrue(seat.reserved)
        

    def can_create_one_show_schedule(self):
        room = Room(1, 20, 15)
        schedule = ShowScheduleShow("Akademia", room, 13, 15, 9, 12, 2023)
        show = Show("Akademia", room, 13, 15, 9, 12, 2023)

    def test_can_create_one_show_schedule(self):
        customer = Customer("anonymous")
        room = Room(1, 20, 15)
        seat = Seat()



def main():
    unittest.main()


if __name__ == "__main__":
    main()



        # Customer
        # Seat
        # Room
        # Ticket
        # Show
        # ShowSchedule