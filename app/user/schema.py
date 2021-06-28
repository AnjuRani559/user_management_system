from marshmallow import fields, Schema
#from click import DateTime


class UserSchema(Schema):


    user_id = fields.Number(attribute="user_id")
    first_name = fields.String(attribute="first_name")
    last_name = fields.String(attribute="last_name")
    full_name = fields.String(attribute="full_name")
    salary = fields.Number(attribute="salary")
    created_at = fields.DateTime(attribute="created_at")

