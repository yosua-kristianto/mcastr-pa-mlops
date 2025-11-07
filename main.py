"""model_builder
This module is responsible for orchestrating building emo analysis model for this project.
This main file, serves as the entry point and orchestrates all required components 
in the model building process.

1. Update Knowledge Base database
2. Fetch data from the database
3. Convert the fetched data into Pandas DataFrame

// These processes below are forked from https://github.com/yosua-kristianto/McAstr/tree/development/McAstr%20ML
4. Data Normalization (Data Pre-Processing)
5. Model Training
6. Model Evaluation
7. Model Saving

"""

from dotenv import load_dotenv
from pipeline import updateKnowledge, load_data, preprocess_data, token_vectorize, data_segmentation

def main():
    load_dotenv()

    updateKnowledge()
    print("[INFO] Knowledge base updated successfully.")
    print("[INFO] Starting data fetching and normalization.")
    
    data = load_data()
    data = preprocess_data(data)
    data = token_vectorize(data)

    # Hardcode bentar
    model = "svc"

    feature_train, feature_test, label_train, label_test, feature_val, label_val = data_segmentation(data, (True if model != "svc" else False))

    if(model == "svc"):
        from svm.trainer import train_test
        train_test(feature_train, feature_test, label_train, label_test)
    elif(model == "lightgbm"):
        from lgb.trainer import train_test
        train_test(feature_train, feature_test, feature_val, label_train, label_test, label_val)
        

    print("[INFO] Model building process completed.")

if __name__ == "__main__":
    from datetime import datetime

    print(f"""
                                                          
|     |___|  _  |___| |_ ___   |     |  |  |     |___ ___ 
| | | |  _|     |_ -|  _|  _|  | | | |  |__|  |  | . |_ -|
|_|_|_|___|__|__|___|_| |_|    |_|_|_|_____|_____|  _|___|
                                                 |_|          
    Session {datetime.now()}
    """)


    main()