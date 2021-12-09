import pandas as pd
from functools import partial


def read_data(csv_path):
    pd_df = pd.read_csv(csv_path)
    return pd_df


def agg_func(df, cat_vars, target_var=None):
    res_dict = {target_var: df[target_var].max()} if target_var is not None else dict()
    for var in cat_vars:
        res_dict[var] = df[var].value_counts().to_dict()
    return pd.DataFrame([res_dict.values()], columns=res_dict.keys())


def aggregate_data(df, user_var, cat_vars, target_var=None):
    agg_df = df.groupby(user_var).apply(partial(agg_func, cat_vars=cat_vars,
                                                target_var=target_var))
    agg_df = agg_df.reset_index().drop("level_1", axis=1).set_index(user_var)
    return agg_df


def check_columns(df, list_columns, exact_check=True):
    check = set(list_columns) == set(df.columns) if exact_check else set(list_columns).issubset(set(df.columns))
    if not check:
        raise(ValueError("The columns of the dataframe are not as expected."))

