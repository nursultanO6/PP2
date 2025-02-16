from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(days = 7)
dif = abs(int((x - y).total_seconds()))
print(dif)
