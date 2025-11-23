from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import GridSearchCV

model = LinearSVC(
    C=10.0,            
    class_weight='balanced',
    max_iter=5000,    
    verbose=True      
)

def run_gridsearch(feature, label):
    """
    Runs GridSearchCV on SVC with parameters C and kernel.
    """
    param_grid = {
        "C": [0.1, 1, 10],              # Regularization strength
        "kernel": ["linear", "rbf"]     # Try linear and RBF kernels
    }

    svc = SVC(max_iter=5000)

    grid_search = GridSearchCV(
        estimator=svc,
        param_grid=param_grid,
        scoring="accuracy",
        cv=3,
        verbose=2,
        n_jobs=-1
    )

    grid_search.fit(feature, label)

    print("Best Parameters:", grid_search.best_params_)
    print("Best Score:", grid_search.best_score_)