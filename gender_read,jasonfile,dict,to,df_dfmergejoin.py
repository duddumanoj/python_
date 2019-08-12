#import json
import pandas as pd



#df = pd.read_json("klm.json") for json files reading
#df = pd.read_json("rt.txt",lines='True')for text files reading
df = pd.read_json("rt.txt",lines='True')


print(df["id"])
print(df.describe())




#Convert the userid columns to string and then try performing the join using the following:
#pd.merge(Userid_train,Useridtourl,left_on="userid",right_on="userid",how='inner')
#df_merged = pd.merge(df, df_urls, on='userid')


