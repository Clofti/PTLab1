from typing import Dict
from Types import DataType

RatingType = Dict[str, str]


class CalcRatingMin90():

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            flag = 1
            for subject in self.data[key]:
                if subject[1] < 90:
                    flag = 0
            if flag == 1:
                self.rating[key] = "Min90"
        return self.rating
