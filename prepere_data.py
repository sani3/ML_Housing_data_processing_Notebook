from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder


def x_y_split(data, label_field):
    x = data.drop(label_field, axis=1)
    y = data[label_field].copy()
    return x, y


def imput_na(data, num_fields, text_fields, strategy="median"):
    imputer = SimpleImputer(strategy=strategy)
    imputer.fit(data[num_fields])
    x_num = imputer.transform(data[num_fields])
    x_num = pd.DataFrame(x_num, columns=num_fields)
    return pd.concat([x_num, data[text_fields]], axis=1)


def encode_ordered_text(data, text_fields):
    ordinal_encoder = OrdinalEncoder()
    x_code = ordinal_encoder.fit_transform(data[text_fields])
    return pd.concat([data.drop(labels=text_fields, axis=1), pd.DataFrame(x_code, columns=text_fields)], axis=1)


def encode_onehot_text(data, text_fields):
    onehot_encoder = OneHotEncoder()
    x_code = onehot_encoder.fit_transform(data[text_fields])
    return pd.concat([data.drop(labels=text_fields, axis=1), pd.DataFrame(x_code.toarray(), columns=onehot_encoder.categories_)], axis=1)
