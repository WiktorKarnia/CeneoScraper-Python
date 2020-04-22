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
# Etap 2 -  pobranie wszystkich opinii z pojedyńczej strony
- zapis składowych opinii od złożonej struktury danych 
# Etap 3 - pobranie wszystkich opinii o pojedyńczym produkcie
-sposób przechodzenia po kolejnych stronach z opiniami
-eksport opinii do pliku (.csv lub .xlsx lub .json)
# Etap 4 - ...
-eliminacja powtarzających się fragmentów kodu
-transformacja danych (typ danych, czyszczenie danych)
# Etap 5 - analiza pobranych danych
-zapis pobranych danych do obiektu dataframe (ramka danych)
-wykonanie prostych obliczeń na danych
-wykonanie prostych wykresów
# Etap 6
-zainstalowanie i uruchamianie Flask'a
-struktura aplikacji /CeneoScraper /run.py /config.py /app /init.py /routes.py /models.py /scraper.py /analyzer.py /static/ /main.css /figures/ /fig.png /templates/ /base.html /opinions /requirements.txt /.venv /README.md
-routing (nawigowanie po stronach serwisu)
-widoki (jinja)
