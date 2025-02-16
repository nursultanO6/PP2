from datetime import datetime, timedelta

x = datetime.now()
d = x - timedelta(days = 5)
print(d)