"""Data Loader File
This file contains the data loading process. If from main being put args 

"""
import pandas

def load_data(env: str):
    """This function loads the `emotions.csv` dataset and prints the 
    first few rows and the count of each column.
    
    If the env is set to 'debug', it this function will trim the dataset
    to only 20 rows.

    Args:
        env (str): The environment setting, e.g., 'debug'.
    Returns:
        DataFrame: The loaded dataset as a pandas DataFrame.
    """
    # The used dataset is from https://www.kaggle.com/datasets/adhamelkomy/twitter-emotion-dataset
    dataframe = pandas.read_csv('emotions.csv')

    # Testing Data Loader for Debugging.
    if(env == 'debug'):
        dataframe = dataframe.sample(n=100000, random_state=42).reset_index(drop=True)

    print(dataframe.head())
    print(f"Count {dataframe.count()}")

    return dataframe

def preprocess_data(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    """This function will performing several steps to process the textual data.
    1. Lowercasing
    2. Removing Punctuation
    3. Removing Stopwords
    4. Stemming

    Args:
        dataframe (DataFrame): The input DataFrame containing the text data.
    Returns:
        DataFrame: The processed DataFrame with cleaned text data.
    """
    import nltk
    from nltk.stem import PorterStemmer
    from nltk.corpus import stopwords

    from tqdm import tqdm

    import string

    # Drop ID column if exists
    if "ID" in dataframe.columns:
        dataframe = dataframe.drop(columns=["ID"])
    
    stemmer = PorterStemmer()
    table = str.maketrans("", "", string.punctuation)

    nltk.download("stopwords", quiet=True)
    stop_words = set(stopwords.words("english"))

    processed_texts = []
    for text in tqdm(dataframe["text"], desc="Preprocessing text", unit="rows"):
        # 1. Lowercase
        text = text.lower()

        # 2. Remove punctuation
        text = text.translate(table)

        # 3. Split by whitespace and stem
        stemmed_tokens = [stemmer.stem(word) for word in text.split()]

        # 4. Stopword removal
        stemmed_tokens = [word for word in stemmed_tokens if word not in stop_words]

        # 5. Join back
        processed_texts.append(" ".join(stemmed_tokens))

    # Replace text column with processed version
    dataframe = dataframe.copy()
    dataframe["text"] = processed_texts

    print("Pre Processing complete. Sample head:")
    print(dataframe.head())

    return dataframe

def token_vectorize(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    """This function will vectorize the text data using HashingVectorizer vectorization.
    Adds a new column 'vectorized' with sparse vectors.

    Args:
        df (pd.DataFrame): Must contain 'text' column
    
    Returns:
        pd.DataFrame: With added 'vectorized' column
    """
    from tqdm import tqdm
    from sklearn.feature_extraction.text import HashingVectorizer
    if "text" not in dataframe.columns:
        raise ValueError("DataFrame must contain a 'text' column")

    # Step 1: Tokenization progress (trivial with sklearn, but simulate with tqdm)
    tqdm.pandas(desc="Tokenizing (uni+bi+trigrams)")
    
    # Step 2: Initialize HashingVectorizer
    vectorizer = HashingVectorizer(
        ngram_range=(1, 3),    # unigrams + bigrams + trigrams
        analyzer="word",
        alternate_sign=False,  # keep values non-negative
        n_features=2**18       # number of features (adjust as needed)
    )

    # Step 3: Vectorization with tqdm
    vectors = []
    for text in tqdm(dataframe["text"], desc="Vectorizing with HashingVectorizer", unit="rows"):
        vec = vectorizer.transform([text])
        vectors.append(vec)

    # Step 4: Save vectorized column
    dataframe = dataframe.copy()
    dataframe["vectorized"] = vectors

    print("Vectorization complete. Sample head:")
    print(dataframe.head())
    
    return dataframe

def data_segmentation(dataframe: pandas.DataFrame, valset: bool = False):
    """
    Splits a DataFrame with 'vectorized' and 'label' columns into
    train/test sets using 70:30 ratio.
    
    Args:
        df (pd.DataFrame): Must contain 'vectorized' and 'label' columns.
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split

    if "vectorized" not in dataframe.columns or "label" not in dataframe.columns:
        raise ValueError("DataFrame must contain 'vectorized' and 'label' columns")
    
    # Convert list of sparse vectors into stacked sparse matrix
    from scipy.sparse import vstack
    X = vstack(dataframe["vectorized"].values)
    y = dataframe["label"].values

    test_size = 0.3 if valset == False else 0.5

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    if(valset):
        X_test, X_val, y_test, y_val = train_test_split(
            X_test, y_test, test_size=0.5, random_state=42, stratify=y_test
        )


    return X_train, X_test, y_train, y_test, X_val, y_val