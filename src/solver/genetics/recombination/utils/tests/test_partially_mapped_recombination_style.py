from dataclasses import dataclass

import pytest

from conftest import TestCase, TestDataBase, TestParameters
from src.solver.genetics.recombination.utils.styles import InPath, partially_mapped_recombination_style


@dataclass
class RecombinationStyleTestData(TestDataBase):
    parent_1: InPath
    parent_2: InPath
    detour_1: int
    detour_2: int
    expected: InPath | type[Exception]


happy_params: TestParameters = TestParameters(
    cases=[
        # TestCase(
        #     id="small_route_with_duplicates",
        #     data=RecombinationStyleTestData(
        #         parent_1={1: 3, 2: 5, 3: 4, 4: 2, 5: 1},
        #         parent_2={1: 2, 2: 3, 3: 5, 4: 1, 5: 4},
        #         expected={1:4, 2:3, 3:5, 4:2, 5:1},
        #         detour_1=2,
        #         detour_2=3,
        #     ),
        # ),
        # TestCase(
        #     id="no_route_correct",
        #     data=RecombinationStyleTestData(
        #         parent_1={},
        #         parent_2={},
        #         expected={},
        #         detour_1=2,
        #         detour_2=3,
        #     ),
        # ),
        TestCase(
            id="small_route_basic",
            data=RecombinationStyleTestData(
                parent_1={1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                parent_2={1: 5, 2: 2, 3: 3, 4: 4, 5: 1},
                expected={1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
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
            data=RecombinationStyleTestData(
                parent_1={},
                parent_2={},
                expected=ValueError,
                detour_1=2,
                detour_2=1,
            ),
        )
    ]
)


@pytest.mark.parametrize(happy_params.get_param_string(), happy_params.get_test_data(), ids=happy_params.get_test_ids())
def test_happy_paths(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int, expected: InPath) -> None:
    assert partially_mapped_recombination_style(parent_1, parent_2, detour_1, detour_2) == expected


@pytest.mark.parametrize(sad_params.get_param_string(), sad_params.get_test_data(), ids=sad_params.get_test_ids())
def test_sad_paths(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int, expected: type[Exception]) -> None:
    with pytest.raises(expected):
        partially_mapped_recombination_style(parent_1, parent_2, detour_1, detour_2)
