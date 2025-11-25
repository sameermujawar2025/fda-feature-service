# app/services/calculators/r3_decline_ratio.py, decline_ratio_last_10min
from app.services.calculators.base import FeatureCalculator
from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector
from app.config.settings import settings


class R3DeclineRatioCalculator(FeatureCalculator):
    """
    R3 – decline_ratio_last_10min
    """

    def __init__(self, repo):
        self.repo = repo

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        total, declines = self.repo.get_txn_stats_last_minutes(
            user_id=txn.user_id,
            card_number=txn.card_number,
            window_minutes=settings.decline_window_minutes,
            now=txn.timestamp
        )

        features.decline_ratio_last_10min = 0.0 if total == 0 else declines / total
