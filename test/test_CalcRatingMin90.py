from typing import Dict, Tuple
from Types import DataType
from CalcRatingMin90 import CalcRatingMin90
import pytest

RatingsType = Dict[str, float]


class TestCalcRating():

    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
            [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],

            "Петров Игорь Владимирович":
            [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],

            "Знайков Матвей Владимирович":
            [
                ("математика", 93),
                ("русский язык", 90),
                ("программирование", 98),
                ("литература", 97)
            ]
        }

        rating_scores: RatingsType = {
            "Знайков Матвей Владимирович": "Min90"
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data:
                              Tuple[DataType,
                                    RatingsType]) -> None:

        calc_rating = CalcRatingMin90(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data:
                  Tuple[DataType, RatingsType]) -> None:

        rating = CalcRatingMin90(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
