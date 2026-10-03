from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_features(train_texts, test_texts):
    # Create the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    # Learn the vocabulary only from the training data
    X_train = vectorizer.fit_transform(train_texts)

    # Transform the test data using the same vocabulary
    X_test = vectorizer.transform(test_texts)

    return X_train, X_test, vectorizer