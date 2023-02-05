from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from validator import validator


@dataclass
class BonusPay(ABC):
    """Represents a basic bonus for a soldier's payment."""

    @abstractmethod
    def get_payment(self) -> int:
        """Returns the bonus to be paid out."""


"""Add your new bonuses here"""


@dataclass
class BonusForManeuvers(BonusPay):
    """Represents a bonus 150 base * number participated, for privates and officers for a field's military maneuvers."""

    maneuvers_number: int = 1
    _maneuvers_base: int = field(init=False, default=150)

    def __post_init__(self) -> None:
        """Validations"""
        validator(self.maneuvers_number)

    def get_payment(self) -> int:
        """Returns the bonus for a field's military maneuvers to be paid out."""
        return 150 * self.maneuvers_number


@dataclass
class BonusForNegotiations(BonusPay):
    """Represents 1000, single bonus for privates and officers for an additional negotiation skills training."""

    _negotiations_base: int = field(init=False, default=1000)

    def get_payment(self) -> int:
        """Returns the bonus for an additional negotiation skills training to be paid out."""
        return self._negotiations_base
