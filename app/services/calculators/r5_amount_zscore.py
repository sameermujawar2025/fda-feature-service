# app/services/calculators/r5_amount_zscore.py,Amount Z-Score
from app.services.calculators.base import FeatureCalculator
from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector


class R5AmountZscoreCalculator(FeatureCalculator):
    """
    R5 – amount_zscore (simple ratio vs last amount)
    """

    def __init__(self, repo):
        self.repo = repo

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        last = self.repo.get_last_successful_txn_for_user_card(
            user_id=txn.user_id,
            card_number=txn.card_number,
            before_time=txn.timestamp
        )
        if not last:
            return

        last_amount = last.get("amount")
        if not last_amount or last_amount <= 0:
            return

        features.amount_zscore = (txn.amount - last_amount) / last_amount
