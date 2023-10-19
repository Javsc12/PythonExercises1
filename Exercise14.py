from datetime import date

f_date = date(1998, 1, 12)
l_date = date(2023, 1, 12)
delta = l_date - f_date
print(delta.days)