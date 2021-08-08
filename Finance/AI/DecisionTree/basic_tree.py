"""
Examples are coming from kaggle introduction of machine learning
"""

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def run_basic_tree():
    # path
    source = 'housing.csv'
    data = pd.read_csv(source)
    print(data.columns)

    features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
    X = data[features]
    y = data['SalePrice']
    # split the data between train and validation data
    # this is not the best way to split as we still need test data
    # normally split is 60:20:20 on small datasets - but hey this is a quick example
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    max_leaf_nodes = [4, 8, 16, 32, 64, 128, 256]
    leaf_err_map = {}

    # train hyper parameter
    for leaf in max_leaf_nodes:
        model = DecisionTreeRegressor(max_leaf_nodes=leaf, random_state=1)
        model.fit(train_X, train_y)
        predictions = model.predict(val_X)
        error = mean_absolute_error(predictions, val_y)
        leaf_err_map[leaf] = error

    # run on all data
    best_num_max_leaf = min(leaf_err_map, key=leaf_err_map.get)
    model = DecisionTreeRegressor(max_leaf_nodes=best_num_max_leaf, random_state=1)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    print(f'error {mean_absolute_error(predictions, val_y): ,.2f}')


if __name__ == '__main__':
    run_basic_tree()
