#import bibliotek
import requests
from bs4 import BeautifulSoup 
# def adres strony z opiniami
url = "https://www.ceneo.pl/76891701#tab=reviews"

# pobieranie kodu HTMl strony z adresu URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text,"html.parser")

# wybranie z kodu strony fragmentów odpowiadajacych poszczegolnym opiniom
opinions = page_tree.select("li.review-box")

opinion = opinions[0]
opinion_id = opinion["data-entry-id"]
# print(opinion_id)
author = opinion.select('div.reviever-name-line')
recomendation = opinion.select('div.product-reviever-summary')
stars = opinion.select('span.review-score-count')
purchased = opinion.select('div.product-review-pz')
useful = opinion.select('button.vote-yes')[0]['data-total-vote'] 
useless = opinion.select('button.vote-no')[0]['data-total-vote'] 
print(useless)

# - opinia: li.review-box
# - identyfikator: li.review-box["data.entry-id"]
# - autor: div.reviever-name-line
# - rekomendacja: div.product-reviever-summary > em
# - liczba gwiazdek: span.review-score-count
# - czy potwierdzona zakupem: div.product-review-pz
# - data wystawienia: span.review-time > time
# ["datetime"] - pierwsze wystapienies
# - data zakupu: span.review-time > time
# ["datetime"] - drugie wystapienie
# - przydatna: button.vote-yes ["data-total-votes"]
# - nieprzydatna: button.vote-no ["data-total-votes"]
# - treść: p.product-review-body
# - wady: div.cons-cell > cons
# - zalety div.pros-cell > pros


# instrukcja skladowych dla pierwszej opini z listy