# app/services/feature_service.py

from typing import List
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector, FeatureResponse

from app.repositories.transaction_repository import TransactionRepository
from app.repositories.blacklist_repository import BlacklistRepository

# ✅ CORRECT NEW CALCULATOR IMPORTS
from app.services.calculators.r1_velocity import R1VelocityCalculator
from app.services.calculators.r2_ip_clustering import R2IPClusteringCalculator
from app.services.calculators.r3_decline_ratio import R3DeclineRatioCalculator
from app.services.calculators.r4_impossible_travel import R4ImpossibleTravelCalculator
from app.services.calculators.r5_amount_zscore import R5AmountZscoreCalculator
from app.services.calculators.r6_country_jump import R6CountryJumpCalculator
from app.services.calculators.r7_hour_of_day import R7HourOfDayCalculator
from app.services.calculators.r8_high_value_flag import R8HighValueFlagCalculator
from app.services.calculators.r9_blacklist_flag import R9BlacklistFlagCalculator

from app.services.calculators.base import FeatureCalculator


class FeatureService:
    """
    Builds the FeatureVector by running all calculators.
    """

    def __init__(
        self,
        txn_repo: TransactionRepository,
        bl_repo: BlacklistRepository
    ):
        self.txn_repo = txn_repo
        self.bl_repo = bl_repo

        # ⚠️ THIS WAS WRONG EARLIER → now corrected
        self.calculators: List[FeatureCalculator] = [
            R1VelocityCalculator(txn_repo),
            R2IPClusteringCalculator(txn_repo),
            R3DeclineRatioCalculator(txn_repo),
            R4ImpossibleTravelCalculator(txn_repo),
            R5AmountZscoreCalculator(txn_repo),
            R6CountryJumpCalculator(txn_repo),
            R7HourOfDayCalculator(),
            R8HighValueFlagCalculator(),
            R9BlacklistFlagCalculator(bl_repo),
        ]

    def compute_features(
        self,
        txn: TransactionRequest
    ) -> FeatureResponse:

        # Empty vector, calculators will update fields
        features = FeatureVector()

        for calc in self.calculators:
            calc.calculate(txn, features)

        return FeatureResponse(features=features)
