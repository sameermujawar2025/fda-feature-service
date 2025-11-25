# app/services/calculators/r6_country_jump.py
from app.services.calculators.base import FeatureCalculator
from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector


class R6CountryJumpCalculator(FeatureCalculator):
    """
    R6 – country_change_flag
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

        last_country = last.get("current_country")
        if not last_country:
            return

        features.country_change_flag = (txn.current_country != last_country)
