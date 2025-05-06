import datetime
today = datetime.date.today()
# using gcd()
class Date:
    """
    Description:
        A class that works with dates. It has methods such as formatting, subtraction, addition, comparison,
        determining leap years, month name, and day of the week name
        (Клас який працює з датами. Має такі методи як форматування, віднімання, додавання, порівняння,
        визначення високосного року, назву місяця і назву дня тижня)
    """
    def __init__(self, day : int, month : int, year : int, description=""):
        """
        Description:
        Initializes a Date class object
        (Ініціалізує об'єкт класу Date)
        Args:
            day (int): day of the month (день місяця)
            month (int): month (місяць)
            year (int): year (рік)
            description (str): date description, default is absent (опис дати, за замовчуванням відсутній)
        Raise:
            ValueError: if the day, month, or year do not match the correct values
            (якщо день, місяць чи рік не відповідають правильним значенням)
            TypeError: if the parameters are not integers (якщо параметри не є цілими числами)
        """
        self._day = day
        self._month = month
        self._year = year
        self._description = description

        if type(day) != int or type(month) != int or type(year) != int:
            raise TypeError("Дані повинні бути числовим значенням")

        if day <=0 or month <= 0 or year <=0:
            raise ValueError("День, місяць і рік не можуть бути від'ємними або дорівнювати 0")

        if month > 12:
            raise ValueError("Місяців у році всього 12!")

        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31
        elif month == 2:
            max_day = 29 if self.is_leap_year() else 28
        else:
            max_day = 30

        if day > max_day:
            raise ValueError(f"У місяці {month}, не може бути {day} днів")


    def __str__(self):
        """
        Description:
            Returns a date string value in the format:
            "dd.mm.yyyy - description" or "dd.mm.yyyy" if no description is provided
            (Повертає рядкове значення дати у форматі:
            "дд.мм.рррр - опис" або "дд.мм.рррр", якщо опис відсутній)
        Return:
            str: in the format dd.mm.yyyy - description or dd.mm.yyyy (у форматі дд.мм.рррр - опис або дд.мм.рррр)
        """
        if self._description:
            return f"{self._day:02d}.{self._month:02d}.{self._year} - {self._description}"
        else:
            return f"{self._day:02d}.{self._month:02d}.{self._year}"


    def __sub__(self, other):
        """
        Description:
            Determines the difference in days between two dates (Визначає різницю в днях між двома датами)
        Return:
            int: difference in days between two dates (різниця в днях між двома датами)
        """
        date = datetime.date(self._year, self._month, self._day)
        difference = date - today
        return difference.days


    def __add__(self, days):
        """
        Description:
            Adds a specified number of days to a date (Додає певну кількість днів до дати)
        Args:
            days (int): number of days to add (кількість днів для додавання)
        Raises:
            TypeError: if the days parameter is not an integer (якщо параметр days не є цілим числом)
        Return:
            str: new date after adding days (нова дата після додавання днів)
        """
        if type(days) != int:
            raise TypeError("Додавати можна тільки ціле число днів")
        date = datetime.date(self._year, self._month, self._day)
        new_date = date + datetime.timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year, self._description)


    def __gt__(self, other):
        """
        Description:
            Compares two dates to see if one date is greater than the other
            (Порівнює дві дати, чи є дата більшою за іншу)
        Return:
            str: string of compared dates (рядок, порівняних дат)
        """
        return (self._year, self._month, self._day) > (other._year, other._month, other._day)


    def __eq__(self, other):
        """
        Description:
            Checks if a date is equal to today's date (Перевіряє, чи дата дорівнює сьогоднішній даті)
        Return:
            str: displays whether that day has come (виводить чи настав цей день)
        """
        date = datetime.date(self._year, self._month, self._day)
        if date == today:
            return f"Цей день настав"


    def is_leap_year(self):
        """
        Description:
            Checks if the year is a leap year (Перевіряє, чи є рік високосним)
        Return:
            bool: True if it is a leap year, False if not (True, якщо рік високосний, False - якщо ні)
        """
        return self._year % 4 == 0


    def month_name(self):
        """
        Description:
            Returns the name of the month with the day and year (Повертає назву місяця з днем і роком)
        Return:
            str: name of the month, day and year (назва місяця, день та рік)
        """
        months_name = ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня",
                     "вересня", "жовтня", "листопада", "грудня"]
        month_name = months_name[self._month - 1]
        return f"{self._day} {month_name} {self._year} рік"


    def day_of_week(self):
        """
        Description:
            Determines the day of the week for a date (Визначає день тижня для дати )
        Return:
            str: day of the week (день тижня)
        """
        days_name = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя']
        date = datetime.date(self._year, self._month, self._day)
        return days_name[date.weekday()]


if __name__ == "__main__":
    try:
        d1 = Date(16, 4, 2025, "Поїздка додому")
        d2 = Date(29, 2, 2025)
        d3 = Date(29, 4, 2025, "Захист лаби")
        print(d3 - today)
        print(d2 + 10)
        print(d1.is_leap_year())
        print(d2.month_name())
        print(d3.day_of_week())
        print(d1 > d2)
        print(d2 == d3)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
