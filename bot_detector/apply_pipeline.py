import sys
import pandas as pd
import pkg_resources
from bot_detector.data import read_data, aggregate_data, check_columns
from bot_detector.pipelines import load_pipeline
from bot_detector.settings import PIPELINE_PKL, USER_VAR, CATEGORICAL_VARS, PROBABILITY_THRESHOLD

def main():
    args = sys.argv
    if len(args) == 3:
        events_pd = read_data(args[1])
        check_columns(events_pd, CATEGORICAL_VARS + [USER_VAR], exact_check=False)
        users_pd = aggregate_data(events_pd, USER_VAR, CATEGORICAL_VARS)
        model = load_pipeline(pkg_resources.resource_filename(__name__, PIPELINE_PKL))
        predictions = (model.predict_proba(users_pd[CATEGORICAL_VARS])[:, 1] >= PROBABILITY_THRESHOLD) * 1
        predictions_pd = pd.DataFrame(index=users_pd.index, data=predictions,
                                      columns=["is_fake_probability"])
        predictions_pd.to_csv(args[2], index=True)
    else:
        raise ValueError("The arguments passed to the module are not valid")


if __name__ == '__main__':
    main()







