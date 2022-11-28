import pytest

from app.catalog.catalog_operations import _normalize_bike_id


@pytest.mark.parametrize("test_input,expected", [("Spectral 125 CF 9", "spectral_125_cf_9"), ("", "")])
def test_normalize_bike_id(test_input, expected):
    assert _normalize_bike_id(test_input) == expected
