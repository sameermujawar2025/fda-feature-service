# app/services/calculators/r9_blacklist_flag.py

from app.services.calculators.base import FeatureCalculator
from app.models.transaction_models import TransactionRequest
from app.models.feature_models import FeatureVector
from app.repositories.blacklist_repository import BlacklistRepository


class R9BlacklistFlagCalculator(FeatureCalculator):
    """
    R9 – blacklist_flag + blacklist_matches
    """

    def __init__(self, repo: BlacklistRepository):
        self.repo = repo

    def calculate(self, txn: TransactionRequest, features: FeatureVector) -> None:
        # Get blacklist matches from DB
        matches = self.repo.find_matches(
            user_id=txn.user_id,
            card_number=txn.card_number,
            ip_address=txn.ip_address
        )

        # NO MATCH → mark safe
        if not matches:
            features.blacklist_flag = False
            features.blacklist_matches = []
            return

        # MATCH FOUND → fraud risk
        features.blacklist_flag = True

        # Convert raw DB entries to safe outward format
        sanitized_matches = []

        for m in matches:
            sanitized_matches.append({
                "user_id": m.get("user_id"),
                "card_number": (
                    str(m.get("card_number"))
                    if m.get("card_number") is not None
                    else None
                ),
                "ip_address": m.get("ip_address"),
                "reason": m.get("reason") or "",
                "source": m.get("source") or "unknown"
            })

        features.blacklist_matches = sanitized_matches
