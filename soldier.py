from dataclasses import dataclass
from typing import Optional, ClassVar

from ranks import Rank
from payment_bonuses import BonusPay


@dataclass
class Soldier:
    """Basic representation of a soldier."""
    _total_payment: ClassVar[int] = 0
    _rank_counter: ClassVar[list] = []

    name: str
    id: int
    rank: Rank
    bonus_pay: Optional[BonusPay] = None
    bonus_pay2: Optional[BonusPay] = None

    """A counter which counts a total number of soldiers and total sum of their payments."""
    def __post_init__(self) -> None:
        self.rank_to_str = str(self.rank)
        Soldier._rank_counter.append(self.rank_to_str)
        Soldier._total_payment += self.compute_pay()

    def compute_pay(self) -> int:
        """Compute how much a soldier should be paid."""
        payout = self.rank.get_payment()
        if self.bonus_pay is not None:
            payout += self.bonus_pay.get_payment()
        if self.bonus_pay2 is not None:
            payout += self.bonus_pay2.get_payment()
        return payout

    @classmethod
    def total_info_about_troops(cls) -> str:
        """Returns information about available soldiers"""
        return f"There are troops in total number of {len(cls._rank_counter)} available:\n" \
               f"{cls._rank_counter.count('Private')} soldiers and {cls._rank_counter.count('Officer')}" \
               f" officers, with total payment of {cls._total_payment}$."

    def __repr__(self) -> str:
        return f'{self.name} is {self.rank} with monthly payment of: {self.compute_pay()}$.'

    def __del__(self) -> None:
        Soldier._rank_counter.remove(self.rank_to_str)
        Soldier._total_payment -= self.compute_pay()
