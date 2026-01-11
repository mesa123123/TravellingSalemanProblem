from pytest_kedge import TestCase, TestSuite

from src.solver.genetics.recombination.utils.styles import order_recombination_style

ordered_recombination_style_tests = TestSuite(
    target=order_recombination_style,
    scenarios=[
        TestCase(
            name="small_route_basic",
            input={
                "parent_1": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                "parent_2": {1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
                "detour_1": 2,
                "detour_2": 5,
            },
            expected={1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
            test_failure_message="The ordered recombination was not calculated correctly for a basic scenario.",
        ),
        TestCase(
            name="no_route_correct",
            input={
                "parent_1": {},
                "parent_2": {},
                "detour_1": 1,
                "detour_2": 5,
            },
            expected={},
            test_failure_message="An empty route should result in an empty route",
        ),
        TestCase(
            name="small_route_conflict",
            input={
                "parent_1": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                "parent_2": {1: 3, 2: 1, 3: 2, 4: 5, 5: 4},
                "detour_1": 2,
                "detour_2": 4,
            },
            expected={1: 3, 2: 1, 3: 2, 4: 5, 5: 4},
            test_failure_message="The ordered recombination was not calculated correctly for a scenario with conflicts.",
        ),
        TestCase(
            name="small_route_long_conflict",
            input={
                "parent_1": {1: 3, 2: 4, 3: 1, 4: 2, 5: 5},
                "parent_2": {1: 5, 2: 3, 3: 2, 4: 5, 5: 1},
                "detour_1": 2,
                "detour_2": 4,
            },
            expected={1: 5, 2: 3, 3: 2, 4: 5, 5: 4},
            test_failure_message="The ordered recombination was not calculated correctly for a scenario with long conflicts.",
        ),
        TestCase(
            name="detour_1_should_be_smaller_or_equal_to_detour_2",
            input={
                "parent_1": {},
                "parent_2": {},
                "detour_1": 2,
                "detour_2": 1,
            },
            expected=ValueError,
            test_failure_message="A ValueError should be raised when detour_1 is greater than detour_2.",
        ),
    ],
)

