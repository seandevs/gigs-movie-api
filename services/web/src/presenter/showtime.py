from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class ShowTimeView:
    id_: int
    date: date
    time: datetime
    price: float

    def json(self):
        return {
                'id': self.id_,
                'date': self.date.isoformat(),
                'time': self.time.isoformat(),
                'price': self.price,
            }
