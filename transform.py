from sklearn.base import BaseEstimator, TransformerMixin


# Custom transformer for  numeric feature scaling
class ScaleNumFields(BaseEstimator, TransformerMixin):
    def __init__(self):  # no *args or **kargs
        self

    def fit(self, x, y=None):
        return self  # nothing else to do

    def transform(self, x, y=None):
        for field in x.columns:
            # min-max scaling also normalization
            x[field] = (x[field] - x[field].min(axis=0)) / (x[field].max(axis=0) - x[field].min(axis=0))
            # Standardization
            # x[field] = (x[field] - x[field].mean(axis=0)) / x[field].std(axis=0)

