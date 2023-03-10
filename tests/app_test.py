from assertpy import assert_that

import app


def test_start_date_is_07_1_2011():
    result = app.START_DATE
    assert_that(result).has_year(2011)
    assert_that(result).has_month(7)
