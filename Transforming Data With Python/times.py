import read
from dateutil.parser import parse 

def parseTime(submission_time):
    return parse(str(submission_time)).hour

df=read.load_data()
submission_hours = df["submission_time"].apply(parseTime)

print(submission_hours.value_counts())

    