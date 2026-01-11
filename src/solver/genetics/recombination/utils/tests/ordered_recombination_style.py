
from pytest_kedge import TestCase, TestSuite
from src.solver.genetics.recombination.utils.styles import InPath, order_recombination_style


@dataclass
class OrderedRecombinationTestData(TestDataBase):
    parent_1: InPath
    parent_2: InPath
    detour_1: int
    detour_2: int
    expected: InPath | Type[Exception]


happy_params: TestParameters = TestParameters(
    cases=[
        TestCase(
            id="small_route_basic",
            data=OrderedRecombinationTestData(
                parent_1={1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                parent_2={1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
                detour_1=2,
                detour_2=5,
                expected={1: 1, 2: 3, 3: 2, 4: 4, 5: 5},
            ),
        ),
        TestCase(
            id="no_route_correct",
            data=OrderedRecombinationTestData(
                parent_1={},
                parent_2={},
                detour_1=1,
                detour_2=5,
                expected={},
            ),
        ),
        TestCase(
            id="small_route_conflict",
            data=OrderedRecombinationTestData(
                parent_1={1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
                parent_2={1: 3, 2: 1, 3: 2, 4: 5, 5: 4},
                detour_1=2,
                detour_2=4,
                expected={1: 3, 2: 1, 3: 2, 4: 5, 5: 4},
            ),
        ),
        TestCase(
            id="small_route_long_conflict",
            data=OrderedRecombinationTestData(
                parent_1={1: 3, 2: 4, 3: 1, 4: 2, 5: 5},
                parent_2={1: 5, 2: 3, 3: 2, 4: 5, 5: 1},
                # {1:3, 2:2, 3:1, 4:5, 5:4}
                # {1:5, 2:3, 3:2, 4:1, 5:1}
                detour_1=2,
                detour_2=4,
                expected={1: 5, 2: 3, 3: 2, 4: 5, 5: 4},
            ),
        ),
    ]
)

sad_params: TestParameters = TestParameters(
    cases=[
        TestCase(
            id="detour_1_should_be_smaller_or_equal_to_detour_2",
            data=OrderedRecombinationTestData(
                parent_1={},
                parent_2={},
                expected=ValueError,
                detour_1=2,
                detour_2=1,
            ),
        )
    ]

