import datetime


date_ = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date_, '%b %d, %Y - %H:%M:%S')
month_date = python_date.strftime('%B')
new_format_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(python_date)
print(month_date)
print(new_format_date)
