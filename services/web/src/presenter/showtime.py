from dataclasses import dataclass
from datetime import date, datetime
from marshmallow import Schema, fields


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


class ShowTimeSchema(Schema):
    id = fields.Int()
    date = fields.Str()
    time = fields.Str()
    price = fields.Float()
