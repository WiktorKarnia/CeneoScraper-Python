from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/scraper')
def scraper():
    return "Podaj kod produktu do pobrania opinii: "

@app.route('/analyzer')
def analyzer():
    return "Podaj kod produktu do analizy: "