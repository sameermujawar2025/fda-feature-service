# app/services/calculators/r7_hour_of_day.py
from app.services.calculators.base import FeatureCalculator
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector


class R7HourOfDayCalculator(FeatureCalculator):
    """
    R7 – hour_of_day
    """

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        features.hour_of_day = txn.timestamp.hour
