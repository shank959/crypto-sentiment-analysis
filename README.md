# Cryptocurrency Market Sentiment Analysis Tool

## Overview
This project is designed to analyze the current sentiment of the cryptocurrency market by leveraging a fine-tuned RoBERTa model. It scrapes news articles from various sources, performs sentiment analysis, and visualizes the results.

## Features
- **Sentiment Analysis**: Uses a fine-tuned RoBERTa model to achieve 98% accuracy in classifying the sentiment of financial articles.
- **Web Scraping**: Utilizes Selenium with ChromeDriver and BeautifulSoup to scrape and extract news articles from multiple sources.
- **Data Visualization**: Employs Matplotlib and Seaborn to create insightful visualizations of sentiment trends.

## Requirements
- Python 3.8+
- ChromeDriver (compatible with your version of Chrome)
- Install the necessary Python packages listed in `requirements.txt`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-sentiment-analysis.git
    cd crypto-sentiment-analysis
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and set up [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) and ensure it's in the projects directory.

## Usage

1. **Run the main.py file that performs webscraping and sentiment analysis**
    ```bash
    python main.py
    ```


