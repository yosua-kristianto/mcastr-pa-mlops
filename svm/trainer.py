from svm.hyperparameter import model

import joblib
from datetime import datetime

from pipeline import evaluation
from config import Log

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
    Log.i(f"Starting SVC model training at {start_timestamp.strftime('%Y%m%d-%H%M%S')}")    

    model.fit(feature_train, label_train)

    timestamp = datetime.now()

    between = int((timestamp - start_timestamp).total_seconds())

    model_name = f"svm-{timestamp.strftime("%Y%m%d-%H%M%S")}"
    filename = f"model-backup/{model_name}.joblib"
    joblib.dump(model, filename)

    Log.i(f"Model saved to {filename}. Starting evaluation...")    
    evaluation(model, model_name, between, feature_test, label_test)