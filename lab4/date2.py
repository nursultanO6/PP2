from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(days = 1)
t = x + timedelta(days = 1)
print(x, y, t)