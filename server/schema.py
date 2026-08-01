from marshmallow import Schema, fields

class UserSchema(Schema) :
    id = fields.Integer()
    username = fields.String()

    tasks = fields.List(fields.Nested(lambda : TaskSchema(exclude=('user',))))


class TaskSchema(Schema) :
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    marked_as_complete = fields.Boolean()
    user = fields.Nested(lambda : UserSchema(exclude=('tasks', )))