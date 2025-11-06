from lightgbm import LGBMClassifier
from sklearn.model_selection import GridSearchCV

model = LGBMClassifier(
    objective = "multiclass", 
    num_class = 6, 
    learning_rate=1e-4,
    n_estimators=200,
    num_leaves=63,
    random_state=42,
)

def run_gridsearch(feature, label):
    """
    Perform hyperparameter tuning on LightGBM using GridSearchCV.
    Returns the best model after tuning.
    """
    # Define parameter grid
    param_grid = {
        "num_leaves": [31, 63, 127],
        "max_depth": [-1, 10, 20],
        "learning_rate": [0.1, 0.05, 0.01],
        "n_estimators": [100, 200, 500],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
    }

    # Grid search
    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="accuracy",
        cv=3,
        verbose=2,
        n_jobs=-1
    )

    grid.fit(feature, label)

    print("Best Parameters:", grid.best_params_)
    print("Best CV Score:", grid.best_score_)