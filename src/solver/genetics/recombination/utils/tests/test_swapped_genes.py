from pytest_kedge import TestCase, TestSuite

from src.solver.genetics.recombination.utils.styles import _swapped_genes

swapped_genes_tests = TestSuite(
    target=_swapped_genes,
    scenarios=[
        TestCase(
            name="small_route_end_index",
            input={
                "parent": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                "detour_1": 2,
                "detour_2": 5,
            },
            expected={1: 0, 2: 2, 3: 3, 4: 4, 5: 5},
            test_failure_message="For small routes with a detour on the last index, we had a fail",
        ),
        TestCase(
            name="no_route_correct",
            input={
                "parent": {},
                "detour_1": 2,
                "detour_2": 3,
            },
            expected={},
            test_failure_message="An empty route should result in an empty route",
        ),
        TestCase(
            name="small_route_basic",
            input={
                "parent": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                "detour_1": 2,
                "detour_2": 3,
            },
            expected={1: 0, 2: 2, 3: 3, 4: 0, 5: 0},
            test_failure_message="The swapped genes were not calculated correctly for a basic scenario.",
        ),
        TestCase(
            name="detour_1_should_be_smaller_or_equal_to_detour_2",
            input={
                "parent": {},
                "detour_1": 2,
                "detour_2": 1,
            },
            expected=ValueError,
            test_failure_message="A ValueError should be raised when detour_1 is greater than detour_2.",
        ),
    ],
)
