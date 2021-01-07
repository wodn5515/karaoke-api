import datetime as dt

class DateTimeFieldUtils:

    def datetimefilter(self, datetime):
        now = dt.datetime.now()
        if now.year != datetime.year:
            return "%y-%m-%d"
        else:
            if now.month == datetime.month and now.day == datetime.day:
                return "%H:%M"
            return "%m-%d"