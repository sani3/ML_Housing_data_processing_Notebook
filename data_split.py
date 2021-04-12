import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split


def rand_split(data):
    train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
    return train_set, test_set


def add_discrete(data, field, new_discrete_field, bins, labels):
    data[new_discrete_field] = pd.cut(
        data[field],
        bins=bins,
        labels=labels
    )


def strat_split(data, new_discrete_field):
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

    for train_index, test_index in split.split(data, data[new_discrete_field]):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]

        for set_ in (strat_train_set, strat_test_set):
            set_.drop(new_discrete_field, axis=1, inplace=True)

        return strat_train_set, strat_test_set
