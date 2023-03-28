import pytest

from app.catalog.catalog_operations import _normalize_bike_id


def test_normalize_bike_id_happy_path():
    test_input = 'Spectral 125 CF 9'
    size = 'M'
    expected = 'spectral_125_cf_9_m'

    assert _normalize_bike_id(test_input, size) == expected


def test_normalize_bike_id_no_data():
    test_input = ''
    size = ''

    with pytest.raises(RuntimeError):
        _normalize_bike_id(test_input, size)
