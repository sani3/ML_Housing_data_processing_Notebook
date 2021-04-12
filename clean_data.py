def remove_samples_with_na_value(data):
    data = data.dropna(
        axis=0, how='any', thresh=None, subset=None, inplace=False
    )
    return data


def remove_unlabeled_samples(data, label_field):
    data = data.dropna(
        axis=0, how='any', thresh=None, subset=[label_field], inplace=False
    )
    return data


def remove_column(data, field_list):
    # field_list is a list of str
    data = data.drop(
        labels=field_list, axis=1, index=None, columns=None,
        level=None, inplace=False, errors='raise'
    )
    return data
