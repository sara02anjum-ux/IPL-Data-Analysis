# import the lib
import matplotlib.pyplot as plt
import pandas as pd
#load the data
df=pd.read_csv("Matplotlib/charts/netflix_dataset_with_nulls.csv")

#clean data
df=df.dropna(subset=["type","release_year","rating","country","duration"])
type_counts=df["type"].value_counts()
plt.figure(figsize=(5,6)) #size of figure
plt.bar(type_counts.index , type_counts.values ,color=["red","orange"])
plt.title("Number of Tv Shows vs Movies")
plt.xlabel("Type")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig("movie vs tv.png")
plt.show()

rating_counts=df["rating"].value_counts()
plt.figure(figsize=(4,5)) #size of figure
plt.pie(rating_counts,labels=rating_counts.index ,autopct="%1.1f%%")
plt.title("Percentage of Tv Shows vs Movies")
plt.tight_layout()
plt.show()

movie_df = df[df["type"] == "Movie"].copy()
# Convert duration properly
movie_df["duration_int"] = movie_df["duration"].str.replace(" min", "")
movie_df["duration_int"] = pd.to_numeric(movie_df["duration_int"], errors='coerce')
# Remove nulls
#movie_df = movie_df.dropna(subset=["duration_int"])
plt.figure(figsize=(6,5))
plt.hist(movie_df["duration_int"], bins=30 , color="pink",edgecolor="black")
plt.title("Movie Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()

release_counts=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index , release_counts.values,color="blue")
plt.title("Release year number of show")
plt.xlabel("Release year")
plt.ylabel("Number of Show")
plt.tight_layout()
plt.show()

country_counts=df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.bar(country_counts.index,country_counts.values,color="green")
plt.title("Top 10 Number of Show")
plt.xlabel("Number of Show")
plt.ylabel("Country")
plt.tight_layout()
plt.show() 

content_by_year=df.groupby(["release_year" , "type"]).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2 , figsize=(12,5))
ax[0].plot(content_by_year.index, content_by_year["Movie"],color="skyblue")
ax[0].set_title("Movie release per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

ax[0].plot(content_by_year.index, content_by_year["TV Show"],color="yellow")
ax[0].set_title("Show release per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of TV Show")

fig.suptitle("compromise TV Show and Movie over released", y=1.02)
plt.tight_layout()
#plt.savefig("movies_tv_show_comparision.png")
plt.show()

