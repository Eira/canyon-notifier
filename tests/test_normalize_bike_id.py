from app.update import normalize_bike_id


def test_normalize_bike_id():
    bike_title = 'Spectral 125 CF 9'

    res = normalize_bike_id(bike_title)

    assert res == 'spectral_125_cf_9'
