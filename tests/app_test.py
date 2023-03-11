from assertpy import assert_that

import app


def test_start_date_is_07_1_2011():
    result = app.START_DATE
    assert_that(result).has_year(2011).has_month(7)


def test_dynamic_life_experience_contains_health_level_and_total_exp():
    result = app.get_dynamic_life_experience()
    assert_that(result.health).is_greater_than(1)
    assert_that(result.total_experience).is_greater_than(1)
    assert_that(result.level).is_greater_than(1)
    assert_that(result.energy).is_equal_to(200)
    assert_that(result.exp_to_next_level).is_greater_than(0).is_less_than(366)
