from datetime import datetime

def date_difference_in_seconds(date1, date2):
    datetime1 = datetime.strptime(date1, "%d-%m-%Y %H:%M:%S")
    datetime2 = datetime.strptime(date2, "%d-%m-%Y %H:%M:%S")
    difference = abs((datetime2 - datetime1).total_seconds())
    return difference


date1 = input("Enter the first date (DD-MM-YYYY HH:MM:SS): ")
date2 = input("Enter the second date (DD-MM-YYYY HH:MM:SS): ")

difference = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference)
