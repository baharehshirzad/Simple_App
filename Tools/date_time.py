from datetime import datetime, date
from persiantools.jdatetime import JalaliDate

now = datetime.now()
# ثانیه رو با round رند میکنیم
sec = round(now.second + now.microsecond / 1000000)
print(f"now time : {now.hour : 02d}:{now.minute : 02d}:{now.second : 02d}")
# تاریخ امروز
today = now.date()
shamsi = JalaliDate(today)
print(f"today date : {shamsi}")