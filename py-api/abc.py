import datetime
import random

numdays = 30
base = datetime.date.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]

date_from = random.choice(date_list)
date_to = random.choice(date_list)
print('Туда ->', date_from)
print('Обратно ->', date_to)

while date_to <= date_from:
    date_to = random.choice(date_list)
    print('Обратно ->', date_to)
