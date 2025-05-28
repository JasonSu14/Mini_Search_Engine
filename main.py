from crawler import fetch_page
from indexer import SearchEngine

if __name__ == "__main__":
    engine = SearchEngine()

    # Example websites to crawl (short pages work best)
    urls = {
        "Python": "https://www.python.org/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "Real Python": "https://realpython.com/"
    }

    print("Crawling and indexing documents...")
    for title, url in urls.items():
        try:
            content = fetch_page(url)
            engine.add_document(title, content)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    engine.build_index()
    print("Ready to search!\n")

    while True:
        query = input("Enter your search query (or 'exit'): ")
        if query.lower() == "exit":
            break
        results = engine.search(query)
        for title, score in results:
            print(f"- {title} ({score[0]:.4f})")
        print()
