import pandas as p 
import numpy as np

data = p.read_csv("data/CRDC2013_14.csv",encoding ="Latin-1")

jj_counts = data["JJ"].value_counts()
sch_counts = data["SCH_STATUS_MAGNET"].value_counts()

jj_df = p.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc=np.sum)

sch_df = p.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc=np.sum)

print(jj_df)
print(sch_df)
