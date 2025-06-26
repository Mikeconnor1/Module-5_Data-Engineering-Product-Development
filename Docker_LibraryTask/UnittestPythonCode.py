import unittest
import pandas as pd
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from python_app import app_refactored  
def enrich_dateDuration(colA, colB, df):
    """
    Enriches the DataFrame with two new columns:
    - 'date_delta': Difference in days between colA and colB.
    - 'valid_loan_flag': Boolean indicating if the loan duration is valid (positive delta).
    Handles missing datetime values gracefully.
    """
    df['date_delta'] = (df[colA] - df[colB]).dt.days
    df['date_delta'] = df['date_delta'].fillna(0)  # Replace NaT differences with 0
    df['valid_loan_flag'] = df['date_delta'] > 0
    return df
class TestLoanDuration(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Book checkout': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01']),
            'Book Returned': pd.to_datetime(['2023-01-10', '2023-01-30', '2023-03-05'])
        })

    def test_date_delta(self):
        result_df = enrich_dateDuration(colA='Book Returned', colB='Book checkout', df=self.df)
        expected_deltas = [9, -2, 4]
        self.assertListEqual(result_df['date_delta'].tolist(), expected_deltas)

    def test_valid_loan_flag(self):
        result_df = enrich_dateDuration(colA='Book Returned', colB='Book checkout', df=self.df)
        expected_flags = [True, False, True]
        self.assertListEqual(result_df['valid_loan_flag'].tolist(), expected_flags)

if __name__ == '__main__':
    unittest.main()