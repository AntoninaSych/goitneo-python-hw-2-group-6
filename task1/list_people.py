from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Створюємо словник для зберігання імен іменинників за днями тижня
    birthdays_by_day = defaultdict(list)

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Визначаємо день початку тижня (понеділок)
    start_of_week = today - timedelta(days=today.weekday())

    # Вихідні - субота і неділя
    weekend_days = [5, 6]  # 5 - субота, 6 - неділя

    # Перебираємо користувачів і аналізуємо їх дати народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Визначаємо дату народження на цьому році
        birthday_this_year = birthday.replace(year=today.year)

        # Перевіряємо, чи день народження вже відбувся цього року
        if birthday_this_year < today:
            # Якщо так, то переносимо його на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Обчислюємо різницю в днях між днем народження та сьогоднішнім днем
        delta_days = (birthday_this_year - today).days

        # Визначаємо день тижня дня народження (переносимо на понеділок, якщо вихідний)
        day_of_week = (start_of_week + timedelta(days=delta_days)).weekday()

        # Якщо день тижня - субота або неділя, то переносимо на понеділок
        if day_of_week in weekend_days:
            day_of_week = 0  # Понеділок

        # Переводимо числове значення дня тижня у текстовий відповідно до календаря Python
        day_name = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][day_of_week]

        # Додаємо ім'я іменинника до відповідного дня тижня
        birthdays_by_day[day_name].append(name)

    # Виводимо результат
    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")
