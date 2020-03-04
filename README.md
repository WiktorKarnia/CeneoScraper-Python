# CeneoScraper
# Etap 1 - pobranie pojedynczeej opinii 
- opinia: li.reviev-box
- identyfikator: li.reviev-box["data.entry-id"]
- autor: div.reviever-name-line
- rekomendacja: div.product-reviever-summary > em
- liczba gwiazdek: span.review-score-count
- czy potwierdzona zakupem: div.product-reviev-pz
- data wystawienia: span.review-time > time
["datetime"] - pierwsze wystapienies
- data zakupu: span.review-time > time
["datetime"] - drugie wystapienie
- przydatna: button.votes-yes ["data-total-votes"]
- nieprzydatna: button.votes-no ["data-total-votes"]
- treść: p.product-reviev-body
- wady: div.cons-cell > cons
- zalety div.pros-cell > pros
