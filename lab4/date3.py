from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(microseconds=5)
print(x, y)