import datetime
from collections import namedtuple

from flask import Flask, render_template

from constants import CHARACTER_STATS

app = Flask(__name__)

START_DATE = datetime.datetime(2011, 7, 1)


@app.route('/')
def index():
    return render_template(
        "index.html",
        dynamic_life_experience=get_dynamic_life_experience(),
        character_stats=CHARACTER_STATS,
    )


def get_dynamic_life_experience():
    dynamic_life_experience = namedtuple(
        "DynamicLifeExperience",
        "health total_experience level energy exp_to_next_level"
    )
    total_experience = _get_total_experience()
    level = _get_level(total_experience)
    return dynamic_life_experience(
        _get_health(level),
        total_experience,
        _get_level(total_experience),
        _get_energy(),
        _get_exp_to_next_level()
    )


def _get_exp_to_next_level():
    today = _get_today()
    pre = datetime.datetime(today.year, START_DATE.month, START_DATE.day)
    post = datetime.datetime(today.year+1, START_DATE.month, START_DATE.day)
    return ((pre if pre > today else post) - today).days


def _get_energy():
    return 200


def _get_health(level: int):
    return level * 73


def _get_total_experience():
    return (_get_today() - START_DATE).days


def _get_level(total_experience: int):
    return total_experience // 365


def _get_today():
    return datetime.datetime.now()


if __name__ == '__main__':
    app.run()
