from unittest import TestCase
from pandas.testing import assert_frame_equal
import pandas as pd
from bot_detector.data import agg_func, aggregate_data
from bot_detector.settings import PIPELINE_PKL, USER_VAR, CATEGORICAL_VARS, TARGET_VAR


class TestTools(TestCase):
    def setUp(self):
        self.input_data_pd = pd.DataFrame(data=[["F7A7BF3761", "click_carrousel", "Phone", 0],
                                                ["BA8F7A71E6", "send_sms", "Motor", 0],
                                                ["21C64F22FC", "send_email", "Jobs", 0],
                                                ["F7A7BF3761", "send_sms", "Phone", 1]],
                                          columns=["UserId", "Event", "Category", "Fake"]
                                          )
        self.output_data_pd = pd.DataFrame(data=[["F7A7BF3761", 1, {"click_carrousel": 1, "send_sms": 1}, {"Phone": 2}],
                                                ["BA8F7A71E6", 0, {"send_sms": 1}, {"Motor": 1}],
                                                ["21C64F22FC", 0, {"send_email": 1}, {"Jobs": 1}]],
                                            columns=["UserId", "Fake", "Event", "Category"]
                                          ).set_index("UserId").sort_index()



    def test_agg_func(self):
        assert_frame_equal(aggregate_data(self.input_data_pd, USER_VAR, CATEGORICAL_VARS, TARGET_VAR).sort_index(),
                           self.output_data_pd)
