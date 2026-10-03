from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_features(train_texts, test_texts):
    # Use individual words and two-word phrases
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )

    # Learn vocabulary only from training data
    X_train = vectorizer.fit_transform(train_texts)

    # Transform test data using the same vocabulary
    X_test = vectorizer.transform(test_texts)

    return X_train, X_test, vectorizer