from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    release_date = fields.Str()
    imdb_rating = fields.Float()
    runtime = fields.Str()
