import calendar


class Kalendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def show(self):
        month_days = calendar.monthrange(self.year, self.month)[1]
        first_week_day = calendar.weekday(self.year, self.month, 1)
        week_length = 7

        week_days = list(calendar.day_name)
        print(" ".join(f"{day}" + "     " for day in week_days))
        print("-" * (7 * 12))

        day = 1
        current_week_day = first_week_day
        while day <= month_days:
            for j in range(week_length):
                if current_week_day > 0:
                    print("{:>7}".format(""), end = "     ")
                    current_week_day -= 1
                elif day <= month_days:
                    print("{:>7}".format(day), end = "     ")
                    day += 1

            print()

if __name__ == "__main__":
    year = 2023
    month = 3
    kalendar = Kalendar(year, month)
    kalendar.show()

