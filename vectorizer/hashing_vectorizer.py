from sklearn.feature_extraction.text import HashingVectorizer

vectorizer = HashingVectorizer(
        ngram_range=(1, 3),    # unigrams + bigrams + trigrams
        analyzer="word",
        alternate_sign=False,  # keep values non-negative
        n_features=2**18       # number of features (adjust as needed)
    )