def format_multiplier(multiplier: float) -> str:
    return f"{multiplier:.2f}x"

def validate_stake(stake: float) -> bool:
    return stake > 0
