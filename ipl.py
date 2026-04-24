import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv("project/IPL.csv")
#print(df.head())
print(df.info())
print(df.shape)#print rows and column
#print(f" your rows are {df.shape[0]} and your column are {df.shape[1]}" )
print(df.isnull().sum())#show null value"""

print(df["match_winner"].value_counts()) # which team won higest match
match_wins=df["match_winner"].value_counts() # print chat
sns.barplot(x=match_wins.index , y=match_wins.values , palette="viridis")
plt.title('most match winning team')
plt.show()

sns.countplot(x=df["toss_decision"],palette="rainbow") 
plt.title("TOSS DECISION")
plt.show()

a=df[df["toss_winner"]==df["match_winner"]]["match_id"].count()
print(a)
percentage=(a*100)/df.shape[0]
print(percentage)

sns.countplot(x=df["won_by"])
plt.title('WON BY RUNS OR WICKETS')
plt.show()

count=df["player_of_the_match"].value_counts().head(10)
plt.figure(figsize=(8,6))
print(count)
sns.barplot(y=count.index ,x= count.values,color="pink",edgecolor="black")
plt.title("top 10 players")
plt.show()

high=df.groupby("top_scorer")["highscore"].sum().sort_values(ascending=False).head(2)
print(high) #max two columns work with use--group by 
#plt.figure(figsize=(5,6))
high.plot(kind="barh")
plt.show()

df["highest_wickets"]=df["best_bowling_figure"].apply(lambda x: x.split("--")[0]) #CREATE NEW COLUMN
df["highest_wickets"]=df["highest_wickets"].astype(int)
top_bowlers=df.groupby("best_bowling")["highest_wickets"].sum().sort_values(ascending=False).head(10)
print(top_bowlers) 
top_bowlers.plot(kind="barh")
plt.title("TOP 10 BOWLERS")
plt.show()

venue_count=df["venue"].value_counts()
print(venue_count)
plt.figure(figsize=(7,4))
sns.barplot(y=venue_count.index ,x= venue_count.values,color="yellow",edgecolor="green")
plt.title("VENUE ")
plt.show()

plt.figure(figsize=(7,4))
venue_count.plot(kind='barh', color='yellow', edgecolor='green')
plt.tight_layout()   # labels ko fit karne ke liye
plt.show()

df=df[df['won_by']=="Runs"].sort_values(by="margin",ascending=False).head(1)[["match_winner" , "margin"]]
print(df)

'''score=df[df["highscore"]==df["highscore"].max()][["top_scorer",'highscore']]
print(score)'''

#df=df[df["highest_wickets"]]==df["highest_wickets"].max()[["best_bowling" , "best_bowling_figure"]]
#print(df)
#print(df.columns)


max_wickets = df["first_ings_wkts"].max()
df_max = df[df["first_ings_wkts"] == max_wickets][["best_bowling", "best_bowling_figure"]]
print(df_max)
