# app/services/calculators/r4_impossible_travel.py,distance + speed validation
from datetime import timezone
from app.services.calculators.base import FeatureCalculator
from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector
from app.utils.geo import haversine_km, compute_speed_kmph


class R4ImpossibleTravelCalculator(FeatureCalculator):
    """
    R4 – distance_from_last_location_km & speed_kmph
    """

    def __init__(self, repo):
        self.repo = repo

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        if txn.current_latitude is None or txn.current_longitude is None:
            return

        last = self.repo.get_last_successful_txn_for_user_card(
            user_id=txn.user_id,
            card_number=txn.card_number,
            before_time=txn.timestamp
        )

        if not last:
            return

        last_lat = last.get("current_latitude")
        last_lon = last.get("current_longitude")
        last_ts = last.get("timestamp")

        if not last_lat or not last_lon or not last_ts:
            return

        if last_ts.tzinfo is None:
            last_ts = last_ts.replace(tzinfo=timezone.utc)
        ts = txn.timestamp.replace(tzinfo=timezone.utc) if txn.timestamp.tzinfo is None else txn.timestamp

        hours = (ts - last_ts).total_seconds() / 3600
        if hours <= 0:
            return

        distance = haversine_km(last_lat, last_lon, txn.current_latitude, txn.current_longitude)
        speed = compute_speed_kmph(distance, hours)

        features.distance_from_last_location_km = distance
        features.speed_kmph = speed
