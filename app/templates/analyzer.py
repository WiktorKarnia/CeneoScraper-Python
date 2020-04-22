#import bibliotek
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#wyświetlanie zawartwości katalogu opinions
print(os.listdir("./app/opinions"))


#wczytanie id produktu którego opinie będą analizowane 
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json("app/opinions/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))

#Wykres słupkowy występowania poszczególnych ocen
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value = 0)
fig, ax = plt.subplots()
stars.plot.bar(color = "magenta")
ax.set_title('Gwiazdki')
ax.set_xlabel('Liczba gwiazdek')
ax.set_ylabel('Liczba opini')
plt.savefig("figures/"+product_id+"_bar.png")
plt.close()

#Udział poszczególnych ocen w ogólnej opini
recommendation = opinions["recommendation"].value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label = "", autopct = "%1.1f%%", colors = ['yellow', 'red'])
ax.set_title('Rekomendacje')
plt.savefig("static/figures/"+product_id+"_pie.png")
plt.close()

average_score = opinions["stars"].mean()
pros = opinions["pros"].count()
cons = opinions["cons"].count()
purchased = opinions["purchased"].sum()

print(average_score, pros, cons, purchased)

stars_purchased = pd.crosstab(opinions["stars"], opinions["purchased"])

print(stars_purchased)