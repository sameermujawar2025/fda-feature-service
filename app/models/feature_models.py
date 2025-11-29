# app/models/feature_models.py
from pydantic import BaseModel
from typing import Optional, List, Dict


class FeatureVector(BaseModel):
    # Velocity / decline
    txn_count_last_10min: Optional[int] = None          # R1
    unique_cards_on_ip: Optional[int] = None            # R2
    decline_ratio_last_10min: Optional[float] = None    # R3

    # Geo / travel
    distance_from_last_location_km: Optional[float] = None  # R4
    speed_kmph: Optional[float] = None                      # R4

    # Behavioural / amount
    amount_zscore: Optional[float] = None               # R5
    country_change_flag: Optional[bool] = None          # R6

    # Real-time only
    hour_of_day: Optional[int] = None                   # R7
    high_value_flag: Optional[bool] = None              # R8



class FeatureResponse(BaseModel):
    features: FeatureVector
