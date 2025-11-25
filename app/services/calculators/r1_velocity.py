# app/services/calculators/r1_velocity.py
from app.services.calculators.base import FeatureCalculator
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector
from app.repositories.transaction_repository import TransactionRepository
from app.config.settings import settings


class R1VelocityCalculator(FeatureCalculator):
    """
    R1 – txn_count_last_10min
    """

    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        if not txn.card_number:
            return

        count = self.repo.count_txns_last_minutes_for_card(
            card_number=txn.card_number,
            window_minutes=settings.velocity_window_minutes,
            now=txn.timestamp
        )
        features.txn_count_last_10min = count
