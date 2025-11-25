from app.services.calculators.r1_velocity import R1VelocityCalculator
from app.services.calculators.r2_ip_clustering import R2IPClusteringCalculator
from app.services.calculators.r3_decline_ratio import R3DeclineRatioCalculator
from app.services.calculators.r4_impossible_travel import R4ImpossibleTravelCalculator
from app.services.calculators.r5_amount_zscore import R5AmountZscoreCalculator
from app.services.calculators.r6_country_jump import R6CountryJumpCalculator
from app.services.calculators.r7_hour_of_day import R7HourOfDayCalculator
from app.services.calculators.r8_high_value_flag import R8HighValueFlagCalculator
from app.services.calculators.r9_blacklist_flag import R9BlacklistFlagCalculator

def build_calculators(txn_repo, blacklist_repo):
    return [
        R1VelocityCalculator(txn_repo),
        R2IPClusteringCalculator(txn_repo),
        R3DeclineRatioCalculator(txn_repo),
        R4ImpossibleTravelCalculator(txn_repo),
        R5AmountZscoreCalculator(txn_repo),
        R6CountryJumpCalculator(txn_repo),
        R7HourOfDayCalculator(),
        R8HighValueFlagCalculator(),
        R9BlacklistFlagCalculator(blacklist_repo),
    ]
