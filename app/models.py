class Product:
    def __init__(self, product_id=None, name=None, opinions=[]):
        self.product_id = product_id
        self.name = name
        self.opinions = opinions


class Opinion:
    selectors = {
            "author": ['div.reviewer-name-line'],
            "recommendation":['div.product-review-summary > em'],
            "stars": ['span.review-score-count'],
            "content":['p.product-review-body'],
            "pros":['div.pros-cell > ul'],
            "cons":['div.cons-cell > ul'],
            "useful":['button.vote-yes', "data-total-vote"],
            "useless":['button.vote-no', "data-total-vote"],
            "purchased":['div.product-review-pz'],
            "purchase_date":['span.review-time > time:nth-of-type(2)', "datetime"],
            "reviev_date":['span.review-time > time:nth-of-type(1)', "datetime"]
    }
    def __init__(self, opinion_id=None, author=None, recomendation=None, stars=None, content=None,
                pros=None, cons=None, useful=None, useless=None, purchased=None, purchase_date=None, review_date=None):
        self.opinion_id = opinion_id
        self.author = author
        self.recomendation = recomendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = useful
        self.useless = useless
        self.purchased = purchased
        self.purchase_date = purchase_date
        self.review_date = review_date
    def __str__(self):
        return f'opinion_id: {self.opinion_id}\n author: {self.author}\n'

    def extract_opinion():
        pass

opinion = Opinion()
print(opinion)