from pytest_kedge import TestCase, TestSuite

from src.solver.genetics.recombination.utils.styles import partially_mapped_recombination_style

test_sutie_partially_mapped_recombination_style = TestSuite(
    target=partially_mapped_recombination_style,
    scenarios=[
        TestCase(
            name="small_route_with_duplicates",
            input={
                "parent_1": {1: 3, 2: 5, 3: 4, 4: 2, 5: 1},
                "parent_2": {1: 2, 2: 3, 3: 5, 4: 1, 5: 4},
                "detour_1": 2,
                "detour_2": 3,
            },
            expected={1: 4, 2: 3, 3: 5, 4: 2, 5: 1},
            test_failure_message="Using a small route with duplicates an error occured",
        ),
        TestCase(
            name="empty_route_with_duplicates",
            input={
                "parent_1": {},
                "parent_2": {},
                "detour_1": 2,
                "detour_2": 3,
            },
            expected={},
            test_failure_message="Using no route, there should be an empty route outputted to the test case",
        ),
        TestCase(
            name="basic_small_route",
            input={
                "parent_1": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                "parent_2": {1: 5, 2: 2, 3: 3, 4: 4, 5: 1},
                "detour_1": 2,
                "detour_2": 3,
            },
            expected={1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
            test_failure_message="Basic Happy Path Failing",
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
            test_failure_message="Value Error is not showing when a the first detour is higher than the second",
        ),
    ],
)
