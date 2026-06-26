import copy

import pytest

from src.app import activities


BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))