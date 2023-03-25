from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint
def get_n_w_s(d: datetime):
    dif_d = 6 -  d.weekday()
    return d + timedelta(days = dif_d)
def prepear_b(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year=datetime.now().year).date()
def get_birthday_per_wk(users):
    birthday_p = defaultdict(list)
    today = datetime.now().date()
    n_w_s = get_n_w_s(today)
    start_time = n_w_s - timedelta(2)
    end_time = n_w_s + timedelta(4)
    happy_u = [user for user in users if start_time <= prepear_b(user['birthday']) <= end_time] 
    for user in happy_u:
        courent_bd: date = prepear_b(user['birthday'])
        if courent_bd.weekday in (5,6):
            birthday_p["Monday"].append(user['name'])
        else:
            birthday_p[courent_bd.strftime('%A')].append(user['name'])
    return birthday_p

users = [{"name": "Akashy", "birthday": "30, 3, 1999"},
        {"name": "Murasuki", "birthday": "14, 4, 1998"},
        {"name": "Aomine", "birthday": "13, 4, 1997"},
        {"name": "Midorima", "birthday": "12, 6, 1996"},
        {"name": "Kise", "birthday": "10, 8, 1995"},
        {"name": "Kuroko", "birthday": "10, 8, 1994"},
        {"name": "Hanamiya", "birthday": "9, 8, 1993"},]

result = get_birthday_per_wk(users)
pprint(result)