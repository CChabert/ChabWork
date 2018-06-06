import pandas as p 
import numpy as np

data = p.read_csv("data/CRDC2013_14.csv",encoding ="Latin-1")

data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]

all_enrollment = data["total_enrollment"].sum()


races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
genders = ["F", "M"]

totals = {}
for race in races:
    race_f = "SCH_ENR_" + race + "_" + genders[0]
    race_m = "SCH_ENR_" + race + "_" + genders[1]
    total_race = "total_" + race 
    totals[total_race] = 100*(data[race_m].sum() + data[race_f].sum()) / all_enrollment

for k,v in totals.items():
    print (k, v)