import read
import collections
#import tldextract

df=read.load_data()

print(df["url"].value_counts())

final_string=""
for index, row in df.iterrows():
    final_string+=str(row["url"])
    final_string+=str(" ")
    
words = final_string.split(" ")

new_words=[]
## Remove nan
for value in words:
    if value=='nan':
        pass
    else:
        new_words.append(value)
        
hundred_domains=collections.Counter(new_words).most_common(100)
print(hundred_domains)
