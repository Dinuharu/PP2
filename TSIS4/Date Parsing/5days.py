from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)
print("Today:",today.strftime("%d-%m-%Y"))
print("Date Five Days Ago:", new_date.strftime("%d-%m-%Y"))
