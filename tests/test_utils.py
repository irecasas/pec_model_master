from unittest import TestCase

import pandas as pd

from pec_model_master.pec_pipelines.feature_engineering.utils import drop_columns, lower_names


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                                'B': {0: 1, 1: 3, 2: 5},
                                'C': {0: 2, 1: 4, 2: 6}})

    def test_drop_columns_ok(self):
        df = self.df.copy()
        drop_columns(df, 'A')
        assert df.shape == (3, 2)
        assert df.columns.to_list() == ['B', 'C']

    def test_lower_names_ok(self):
        df = self.df.copy()
        lower_names(df)
        assert df.shape == self.df.shape
        assert df.columns.to_list() == ['a', 'b', 'c']
