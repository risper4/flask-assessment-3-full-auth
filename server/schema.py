from marshmallow import Schema, fields

class UserSchema(Schema) :
    id = fields.Integer()
    username = fields.String()

    posts = fields.List(fields.Nested(lambda : TaskSchema(exclude=('user',))))


