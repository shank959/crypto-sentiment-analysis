from flask import Flask, request, render_template, redirect, url_for
from utils.sentiment_analysis import sentiment_scores, sentiment_count
from utils.webscrape import scrape_news
from utils.helper import create_pie_chart

app = Flask(__name__)

@app.route('/')
def index():
    coin_options = [
        "Bitcoin",
        "Ethereum",
        "Solana",
        "Dogecoin",
        "Cardano",
        "Tether",
        "Tron",
        "Polkadot",
        "Chainlink",
        "Polygon",
        "Litecoin"
    ]
    return render_template('index.html', coin_options=coin_options)


@app.route('/analyze', methods=['POST'])
def analyze():

    coin = request.form['coin']
    articles = scrape_news(coin_name=coin, num_pages=3)
    sentiments = sentiment_scores(articles)
    counts = sentiment_count(sentiments)
    fig_html = create_pie_chart(counts)
   
    return render_template('results.html', coin=coin, sentiments=sentiments, articles=articles, counts=counts, fig_html=fig_html)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
