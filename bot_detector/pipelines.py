from sklearn.base import BaseEstimator, TransformerMixin
from joblib import dump, load
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables_to_drop, axis=1)

        return X


class CalculateCategoricalVariance(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].map(lambda x: np.var(list(x.values())))
        return X


class CountSubcategories(BaseEstimator, TransformerMixin):

    def __init__(self, col_name, cat_var, subcategories=None):
        self.subcategories = subcategories
        self.col_name = col_name
        self.cat_var = cat_var

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        if self.subcategories is not None:
            X[self.col_name] = X[self.cat_var].map(lambda x: np.sum([x.get(cat, 0) for cat in self.subcategories]))
        else:
            X[self.col_name] = X[self.cat_var].map(lambda x: np.sum(list(x.values())))
        return X


def save_pipeline(save_filename, pipeline_to_persist):
    # Prepare versioned save file name
    dump(pipeline_to_persist, save_filename)


def load_pipeline(file_name):
    return load(file_name)

users_pipe = Pipeline(
    [
        ('count_events',
         CountSubcategories(col_name="EventCount", cat_var="Event")),
        ('calculate_categories_variance',
         CalculateCategoricalVariance(["Category"])),
        ('calculate_event_skewness',
         CountSubcategories(col_name="EventSkewness", cat_var="Event",
                            subcategories=["click_ad", "send_email"])),
        ('drop_features',
         DropUnecessaryFeatures(variables_to_drop=["Event"])),
        ('lr_model',
         LogisticRegression(random_state=0))
    ]
)

CountSubcategories.__module__ = "bot_detector.pipelines"
CalculateCategoricalVariance.__module__ = "bot_detector.pipelines"
DropUnecessaryFeatures.__module__ = "bot_detector.pipelines"
