from svm.hyperparameter import model

import joblib
from datetime import datetime

from evaluator import evaluation

def train_test(feature_train, feature_test, label_train, label_test):
    """
    Train and test an SVC model.

    Args:
        feature_train: Training features
        feature_test: Testing features
        label_train: Training labels
        label_test: Testing labels

    Returns:
        model: Trained SVC model
        results: Dict with accuracy, confusion matrix, and classification report
    """
    start_timestamp = datetime.now()
    print(f"[INFO] Start training SVC model {start_timestamp.strftime("%Y%m%d-%H%M%S")}")

    model.fit(feature_train, label_train)

    timestamp = datetime.now()

    between = int((timestamp - start_timestamp).total_seconds())

    model_name = f"svm-{timestamp.strftime("%Y%m%d-%H%M%S")}"
    filename = f"{model_name}.joblib"
    joblib.dump(model, filename)

    print(f"[INFO] Model saved to {filename}")

    print("[INFO] Evaluating SVM model...")
    evaluation(model, model_name, between, feature_test, label_test)