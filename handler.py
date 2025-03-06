from datetime import datetime
import json

class TransactionHandler:
    @staticmethod
    def parse_csv(line):
        fields = line.split(',')
        return {
            'timestamp': fields[0],  
            'origin': fields[1],     
            'destination': fields[2],
            'transaction_amount': float(fields[3])
        }

    @staticmethod
    def filter_out_transactions_amount(transaction):
        """Filters out transactions with an amount greater than 20."""
        return transaction['transaction_amount'] > 20

    @staticmethod
    def filter_out_transactions_before_2010(transaction):
        """Filters out transactions before the year 2010."""
        year = int(transaction['timestamp'][:4])  # Extract YYYY from "YYYY-MM-DD"
        return year >= 2010

    @staticmethod
    def extract_date(element):
        """Extracts the date from the timestamp."""
        timestamp = datetime.strptime(element['timestamp'], '%Y-%m-%d %H:%M:%S UTC').strftime('%Y-%m-%d')
        amount = element['transaction_amount']
        return timestamp, amount

    @staticmethod
    def format_as_json(date_amount):
        """Formats output as JSON."""
        date, total_amount = date_amount
        return json.dumps({"date": date, "total_amount": total_amount})