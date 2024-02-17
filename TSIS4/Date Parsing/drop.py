from datetime import datetime
def drop_microseconds(dt):
    return dt.replace(microsecond=0)

with_microseconds = datetime(2024, 2, 13, 11, 22, 33, 123456)
without_microseconds = drop_microseconds(with_microseconds)

print("Datetime with microseconds:", with_microseconds)
print("Datetime without microseconds:", without_microseconds)
