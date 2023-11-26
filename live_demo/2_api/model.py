from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import pickle as pkl

def build_model(dataset_path, target, seed, model_save_path):
    # Load the dataset
    data = pd.read_csv(dataset_path)

    # One-hot encode categorical features
    ohe = OneHotEncoder(sparse_output=False)
    print(data)
    ohe.fit(data[['material', 'process']])
    data = pd.concat([
        data.drop(['material', 'process'], axis=1),
        pd.DataFrame(ohe.transform(data[['material', 'process']]), columns=ohe.get_feature_names_out(['material', 'process']))
    ], axis=1)
    

    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(target, axis=1),
        data[target],
        test_size=0.2,
        random_state=seed
    )

    # Train the model
    model = GradientBoostingRegressor(random_state=SEED)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"RMSE: {rmse:.2f} min")

    # Save the model and the list of encoded columns
    with open(model_save_path, 'wb') as file:
        pkl.dump((ohe, model), file)
    
    return model

if __name__ == '__main__':
    SEED = 0
    DATASET_PATH = 'dataset.csv'
    TARGET = 'time_min'
    MODEL_PATH = 'model.pkl'

    model = build_model(DATASET_PATH, TARGET, SEED, MODEL_PATH)