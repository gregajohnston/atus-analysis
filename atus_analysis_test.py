import unittest
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from atus_analysis import importer

df_init = importer()
class AtusAnalysisTest(unittest.TestCase):

    def test_read_data(self):
        df = df_init
        self.assertEqual(type(df), pd.DataFrame)
        self.assertEqual(type(df['tucaseid']), pd.Series)

    def test_data_type(self):
        df = df_init
        self.assertEqual(type(df['tucaseid'][0]), np.int64)
        self.assertEqual(type(df['t010101'][0]), np.int64)

    def test_data_width(self):
        df = df_init
        self.assertEqual(len(df.columns), 409)

if __name__ == '__main__':
    unittest.main()
