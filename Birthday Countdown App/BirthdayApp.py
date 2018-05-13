# Python Birthday App

import datetime

def get_user_birthday():
    year = int(input('What year were you born? [YYYY]: '))
    month = int(input('What month were you born? [MM]: '))
    day = int(input('What day were you born? [DD]: '))

    birthday = datetime.date(year, month, day)
    
    return birthday

def date_delta(birthday, today):
    bday_this_year = datetime.date(year=today.year, month=birthday.month, day=birthday.day)
    delta = bday_this_year - today
    
    return delta.days

def print_birthday_info(days):
    if days < 0:
        print('\nYou had your birthday {} days ago this year.'.format(days))
    elif days > 0:
        print('\nYour birthday is in {} days!'.format(days))
    else:
        print('\nHappy birthday!!!')
        
if __name__ == '__main__':
    birthday = get_user_birthday()
    thisday = datetime.date.today()
    days = date_delta(birthday, thisday)
    print_birthday_info(days)