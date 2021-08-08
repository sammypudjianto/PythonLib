from sklearn.essemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def score_dateset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state = 0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)
