import datetime

class DateFormat:
    @classmethod
    def convert_date(cls, date_str):
        date = datetime.datetime.strptime(date_str, "%Y/%m/%d").date()
        return datetime.datetime.strftime(date, "%Y/%m/%d")
