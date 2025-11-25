# app/api/feature_router.py
from fastapi import APIRouter, Depends
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureResponse
from app.services.feature_service import FeatureService
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.blacklist_repository import BlacklistRepository


router = APIRouter(
    prefix="/api/v1/features",
    tags=["features"]
)


def get_feature_service() -> FeatureService:
    # simple DI (can swap later for container)
    txn_repo = TransactionRepository()
    bl_repo = BlacklistRepository()
    return FeatureService(txn_repo, bl_repo)


@router.post("/compute", response_model=FeatureResponse)
def compute_features(
    request: TransactionRequest,
    service: FeatureService = Depends(get_feature_service)
) -> FeatureResponse:
    """
    Compute all features (R1–R9) for a transaction.

    Request (simplified):
    {
      "transaction_id": "TXN123",
      "timestamp": "2025-11-21T10:00:00Z",
      "user_id": "U001",
      "card_number": "4111111111111111",
      "amount": 14500.75,
      "currency": "INR",
      "txn_status": "APPROVED",
      "ip_address": "192.168.1.10",
      "current_latitude": 12.97,
      "current_longitude": 77.59,
      "current_country": "IN"
    }

    Response:
    {
      "features": {
        "txn_count_last_10min": 4,
        "unique_cards_on_ip": 3,
        "decline_ratio_last_10min": 0.25,
        "distance_from_last_location_km": 845.3,
        "speed_kmph": 912.5,
        "amount_zscore": 3.2,
        "country_change_flag": true,
        "hour_of_day": 3,
        "high_value_flag": true,
        "blacklist_flag": false,
        "blacklist_matches": []
      }
    }
    """
    return service.compute_features(request)
