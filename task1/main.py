from datetime import datetime
import list_people
import chat


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 1)},
]


list_people.get_birthdays_per_week(users)
chat.main()
