from abc import ABC
from dataclasses import astuple, dataclass, fields
from typing import Any


@dataclass
class TestDataBase(ABC):
    expected: Any


@dataclass
class TestCase:
    id: str
    data: TestDataBase


@dataclass
class TestParameters:
    cases: list[TestCase]

    def get_param_string(self) -> str:
        return ", ".join([field.name for field in fields(self.cases[0].data)])

    def get_test_ids(self) -> list[str]:
        return [case.id for case in self.cases]

    def get_test_data(self) -> list[tuple]:
        return [astuple(case.data) for case in self.cases]
