from pydantic import BaseModel


class TransactionModel(BaseModel):
    timestamp: str
    origin: str
    destination: str
    transaction_amount: float