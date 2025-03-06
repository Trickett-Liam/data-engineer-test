import unittest
import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from main import TransactionProcessing

class TransactionProcessingTest(unittest.TestCase):
    def test_transaction_processing(self):
        input_data = [
            "date,origin,destination,transaction_amount",  
            "2011-01-01 00:00:00 UTC,AccountA,AccountB,50", 
            "2009-12-31 00:00:00 UTC,AccountC,AccountD,100", 
            "2012-06-15 00:00:00 UTC,AccountE,AccountF,30", 
            "2013-03-10 00:00:00 UTC,AccountG,AccountH,10"
        ]

        expected_output = [
            '{"date": "2011-01-01", "total_amount": 50.0}',
            '{"date": "2012-06-15", "total_amount": 30.0}'
        ]

        with TestPipeline() as p:
            input_pcoll = p | beam.Create(input_data[1:])  # Skip header
            output_pcoll = input_pcoll | TransactionProcessing()

            assert_that(output_pcoll, equal_to(expected_output))

if __name__ == "__main__":
    unittest.main()