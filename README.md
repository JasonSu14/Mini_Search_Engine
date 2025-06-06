# Mini Search Engine

A very basic search engine from scratch in Python to learn the fundamentals of how systems like Google Search work — including crawling, indexing, and keyword-based ranking using TF-IDF.

I started building this tiny project because I was wondering how Safari always used Google Search as its default search engine, and how any search engine works. To understand it better, I decided to build this project to enhance my understanding of a search engine.

## Features

- Crawl webpages (using `requests` + `BeautifulSoup`)
- Extract and clean up main text content
- Index documents using `TfidfVectorizer`
- Search and rank results by relevance (TF-IDF)
- Simple CLI (command-line interface) for querying

## What Does Each File Do?

`crawler.py`: This file handles downloading web pages (through HTTP GET request) and extracting readable text from HTML. In a real search engine, crawling is the first step: take Google as example, the crawlers (e.g. Googlebot) are used to visit billions of pages to gather content.

`indexer.py`: This file builds the index: the core data structure that enables fast and relevant searches. We use TF-IDF (Term Frequency-Inverse Document Frequency) to rank the results on how relevant it is to the search term. We do this because search engines don't scan raw text at query time as that's too slow. Instead, we pre-process documents into an index so we can quickly match queries to relevant content.

`main.py`: This is the script that controls the entire workflow of the search engine as well as provide the CLI for querying. It contains a small dictionary of URLs (this is our "web") and uses the crawler to get the content and add them to the index.

## First-time Setup Guide (Linux / MacOS)

1. Clone this repository

    ```bash
    git clone https://github.com/JasonSu14/Mini_Search_Engine.git
    cd Mini_Search_Engine
    ```

2. Create a virtual environment

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment

   ```bash
   source venv/bin/activate
   ```

4. Install required dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Deactivate when you're done

   ```bash
   deactivate
   ```

## How to Run?

1. Run the code

   ```bash
   python3 main.py
   ```

2. Then type in a search query like:

   `Enter your search query (or 'exit'): python language`

3. See the results

   Now it will return a list of the top matching pages and their relevance scores.

## For Developers

- Every time you want to work on the project: `source venv/bin/activate`

- When you're done: `deactivate`

## Contributors

- Jason Su ([su.925@buckeyemail.osu.edu](mailto:su.925@buckeyemail.osu.edu)) - Code & Implementation
