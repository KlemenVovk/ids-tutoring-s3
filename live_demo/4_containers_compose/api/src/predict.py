import pickle
import pandas as pd
import argparse

def predict_one(model_path, x_cm, y_cm, z_cm, material, complexity, process):
    ohe, model = None, None
    with open(model_path, 'rb') as file:
        ohe, model = pickle.load(file)
    
    # Create a DataFrame with the input data
    data = pd.DataFrame({
        'x_cm': [x_cm],
        'y_cm': [y_cm],
        'z_cm': [z_cm],
        'material': [material],
        'complexity': [complexity],
        'process': [process]
    })

    # One-hot encode categorical features
    data = pd.concat([
        data.drop(['material', 'process'], axis=1),
        pd.DataFrame(ohe.transform(data[['material', 'process']]), columns=ohe.get_feature_names_out(['material', 'process']))
    ], axis=1)

    # Make the prediction
    y_pred = int(model.predict(data)[0])

    return y_pred

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict the production time for a given part')
    # required arguments
    parser.add_argument('model_path', type=str, help='Path to the model file')
    parser.add_argument('x_cm', type=float, help='X dimension of the part (in cm)')
    parser.add_argument('y_cm', type=float, help='Y dimension of the part (in cm)')
    parser.add_argument('z_cm', type=float, help='Z dimension of the part (in cm)')
    parser.add_argument('material', type=str, help='Material of the part')
    parser.add_argument('complexity', type=int, help='Complexity of the part')
    parser.add_argument('process', type=str, help='Machining process used to manufacture the part')
    args = parser.parse_args()
    y_pred = predict_one(args.model_path, args.x_cm, args.y_cm, args.z_cm, args.material, args.complexity, args.process)
    print(f"Predicted production time: {y_pred} min")