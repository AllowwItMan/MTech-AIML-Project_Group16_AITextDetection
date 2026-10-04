from sklearn.linear_model import LogisticRegression


def create_model():
    # Create the Logistic Regression classifier
    model = LogisticRegression(max_iter=1000)

    return model


def train_model(model, X_train, y_train):
    # Train the model using the training data
    model.fit(X_train, y_train)

    return model


def predict(model, X_test):
    # Predict whether each passage is human (0) or AI (1)
    predictions = model.predict(X_test)

    return predictions