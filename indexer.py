from sklearn.feature_extraction.text import TfidfVectorizer

class SearchEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english') # removes common English words that don't help search relevance
        self.document = [] # a list of text contents of the webpages
        self.titles = [] # a list of document titles
        self.tfidf_matrix = None # a matrix of TF-IDF scores that stores the indexed form of all documents
    
    def add_document(self, title, text):
        self.titles.append(title)
        self.document.append(text)

    # building the searchable vector representation
    def build_index(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.document) # converts all added documents into TF-IDF vectors

    def search(self, query, top_k = 5):
        query_vec = self.vectorizer.transform([query]) # this vector represents the importance of each word in the query
        scores = (query_vec.dot(self.tfidf_matrix.T)).T.toarray() # calculates the dot product (similarity) between the query and every document
        ranked = sorted(
            zip(self.titles, scores),
            key = lambda x: -x[1][0] # sort by descending TF-IDF score (highest-ranked document first)
        )
        return ranked[:top_k]
