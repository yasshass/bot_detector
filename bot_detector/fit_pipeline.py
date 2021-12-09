import sys
import pandas as pd
from bot_detector.data import read_data, aggregate_data, check_columns
from bot_detector.pipelines import (load_pipeline, save_pipeline, users_pipe)
from bot_detector.settings import PIPELINE_PKL, USER_VAR, CATEGORICAL_VARS, TARGET_VAR


def main():
    args = sys.argv
    if len(args) == 3:
        events_pd = read_data(args[1])
        check_columns(events_pd, CATEGORICAL_VARS + [USER_VAR, TARGET_VAR], exact_check=False)
        users_pd = aggregate_data(events_pd, USER_VAR, CATEGORICAL_VARS, TARGET_VAR)
        users_pipe.fit(users_pd[CATEGORICAL_VARS], users_pd[TARGET_VAR])
        save_pipeline(args[2], users_pipe)
    else:
        raise ValueError("The arguments passed to the module are not valid")


if __name__ == '__main__':
    main()