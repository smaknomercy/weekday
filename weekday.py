from datetime import date
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'uk_UA')
today = date.today()
print("Сьогодні {}-й день тижня, {}!".format(
    today.weekday(),
    calendar.day_name[today.weekday()]))