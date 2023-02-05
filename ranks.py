from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from validator import validator


class Rank(ABC):
    """Represents a military rank and a payment process for a particular soldier."""

    @abstractmethod
    def get_payment(self) -> int:
        """Compute how much to pay a soldier under this rank."""


"""Add your new ranks here"""


@dataclass(repr=False)
class Private(Rank):
    """Represents rank and payment process for a private's rank soldier."""
    hourly_pay_rate: int = 0
    hours_worked: int = 0
    _base_pay_rate: int = field(init=False, default=1000)

    def __post_init__(self) -> None:
        """Validations"""
        validator(self.hourly_pay_rate, self.hours_worked)

    def get_payment(self) -> int:
        return self._base_pay_rate + self.hourly_pay_rate * self.hours_worked

    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclass(repr=False)
class Officer(Rank):
    """Represents rank and payment process for an officer's rank soldier."""
    hourly_pay_rate: int = 0
    hours_worked: int = 0
    _base_pay_rate: int = field(init=False, default=4000)

    def __post_init__(self) -> None:
        """Validations"""
        validator(self.hourly_pay_rate, self.hours_worked)

    def get_payment(self) -> int:
        return self._base_pay_rate + self.hourly_pay_rate * self.hours_worked

    def __repr__(self) -> str:
        return self.__class__.__name__
