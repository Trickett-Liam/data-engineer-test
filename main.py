import apache_beam as beam
import logging
from apache_beam.options.pipeline_options import PipelineOptions
from handler import TransactionHandler

logging.basicConfig(level=logging.INFO)

class TransactionProcessing(beam.PTransform):
    """Composite Transform to process transactions"""

    def expand(self, pcoll):
        return (
            pcoll
            | "Parse CSV" >> beam.Map(TransactionHandler.parse_csv)
            | "Filter Amount > 20" >> beam.Filter(TransactionHandler.filter_out_transactions_amount)
            | "Filter Year >= 2010" >> beam.Filter(TransactionHandler.filter_out_transactions_before_2010)
            | "Extract Date" >> beam.Map(TransactionHandler.extract_date)
            | "Sum By Date" >> beam.CombinePerKey(sum)
            | "Format as JSON" >> beam.Map(TransactionHandler.format_as_json)
        )

def run_pipeline():
    logging.info("Starting Apache Beam pipeline...")

    options = PipelineOptions()
    
    try:
        with beam.Pipeline(options=options) as p:
            (
                p
                | "Read CSV" >> beam.io.ReadFromText(
                    "gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv",
                    skip_header_lines=1
                )
                | "Process Transactions" >> TransactionProcessing()
                | "Write Output" >> beam.io.WriteToText(
                    "output/results",
                    num_shards=1,
                    shard_name_template="", 
                    file_name_suffix=".jsonl.gz",
                    compression_type=beam.io.filesystem.CompressionTypes.GZIP
                )
            )

        logging.info("Pipeline execution completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}", exc_info=True)

if __name__ == "__main__":
    run_pipeline()
