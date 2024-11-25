import datetime
from calendar import month

now = datetime.datetime.now()
n_month = now.month

if 2 < n_month <6:
    print("봄")
elif 5 < n_month < 9:
    print("여름")
elif 8< n_month<12:
    print("가을")
else:
    print("겨울")