import datetime

def days_until_birthday(month, day):
    today = datetime.date.today()
    birthday = datetime.date(today.year, month, day)

    if birthday < today:
        birthday = datetime.date(today.year + 1, month, day)
    
    diff = birthday - today
    return diff.days

def birthday_message(name, month, day):
    days = days_until_birthday(month, day)
    print(f"Hello {name}! Your birthday is in {days} days.")

birthday_message("Jason", 10, 28)
