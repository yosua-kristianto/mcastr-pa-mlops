from lgb.hyperparameter import model
from datetime import datetime

import joblib
from pipeline import evaluation

def train_test(feature_train, feature_test, feature_val, label_train, label_test, label_val):
    """
    Train and test an LightGBM model.

    Args:
        feature_train: Training features
        feature_test: Testing features
        feature_val: Validation Features
        label_train: Training labels
        label_test: Testing labels
        label_val: Validation labels

    Returns:
        model: Trained LightGBM model
        results: Dict with accuracy, confusion matrix, and classification report
    """
    start_timestamp = datetime.now()
    print(f"[INFO] Start training LightGBM model {start_timestamp.strftime("%Y%m%d-%H%M%S")}")

    model.fit(
        feature_train, label_train,
        eval_set = [(feature_val, label_val)],
        eval_metric = "multi_logloss"
    )

    timestamp = datetime.now()

    between = int((timestamp - start_timestamp).total_seconds())

    model_name = f"lgb-{timestamp.strftime("%Y%m%d-%H%M%S")}"
    filename = f"{model_name}.joblib"
    joblib.dump(model, filename)

    print(f"[INFO] Model saved to {filename}")

    print("[INFO] Evaluating LightGBM model...")
    evaluation(model, model_name, between, feature_test, label_test)
