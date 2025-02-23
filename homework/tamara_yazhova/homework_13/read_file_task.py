import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(filepath):
    with open(filepath, encoding="utf-8-sig") as eugene_file:
        for line in eugene_file:
            yield line


for i, line in enumerate(read_file(eugene_file_path), start=1):
    parts = line.split(' - ')
    new_date = parts[0].split(maxsplit=1)[1]
    date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S.%f")

    if i == 1:
        week_ago = date_obj + datetime.timedelta(days=7)
        print(week_ago)

    elif i == 2:
        print(date_obj.strftime('%A'))

    elif i == 3:
        days_ago = (datetime.datetime.now() - date_obj).days
        print(days_ago)
