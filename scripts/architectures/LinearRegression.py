import pickle

from sklearn.linear_model import LinearRegression


def LRModel(cfg: dict, load_model=False, filename=None, X=None, y=None):
    if load_model:
        loaded_model = pickle.load(open(filename, "rb"))
        return loaded_model

    else:
        model = LinearRegression(
            fit_intercept=bool(cfg["params"]["fit_intercept"]),
            copy_X=bool(cfg["params"]["copy_X"]),
            n_jobs=cfg["params"]["n_jobs"],
            positive=bool(cfg["params"]["positive"]),
        )
        model.fit(X, y)
        return model
