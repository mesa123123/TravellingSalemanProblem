from dataclasses import dataclass
from typing import Type

import pytest

from conftest import TestCase, TestDataBase, TestParameters
from src.solver.genetics.recombination.utils.styles import InPath, _swapped_genes


@dataclass
class SwapGenesTestData(TestDataBase):
    parent: InPath
    detour_1: int
    detour_2: int
    expected: InPath | Type[Exception]


happy_params: TestParameters = TestParameters(
    cases=[
        TestCase(
            id="small_route_end_index",
            data=SwapGenesTestData(
                parent={1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                expected={1: 0, 2: 2, 3: 3, 4: 4, 5: 5},
                detour_1=2,
                detour_2=5,
            ),
        ),
        TestCase(
            id="no_route_correct",
            data=SwapGenesTestData(
                parent={},
                expected={},
                detour_1=2,
                detour_2=3,
            ),
        ),
        TestCase(
            id="small_route_basic",
            data=SwapGenesTestData(
                parent={1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                expected={1: 0, 2: 2, 3: 3, 4: 0, 5: 0},
                detour_1=2,
                detour_2=3,
            ),
        ),
    ]
)
sad_params: TestParameters = TestParameters(
    cases=[
        TestCase(
            id="detour_1_should_be_smaller_or_equal_to_detour_2",
            data=SwapGenesTestData(
                parent={},
                expected=ValueError,
                detour_1=2,
                detour_2=1,
            ),
        )
    ]
)

# 3 2 1


@pytest.mark.parametrize(happy_params.get_param_string(), happy_params.get_test_data(), ids=happy_params.get_test_ids())
def test_happy_paths(parent: InPath, detour_1: int, detour_2: int, expected: InPath) -> None:
    assert _swapped_genes(parent, detour_1, detour_2) == expected


@pytest.mark.parametrize(sad_params.get_param_string(), sad_params.get_test_data(), ids=sad_params.get_test_ids())
def test_sad_paths(parent: InPath, detour_1: int, detour_2: int, expected: type[Exception]) -> None:
    with pytest.raises(expected):
        _swapped_genes(parent, detour_1, detour_2)
