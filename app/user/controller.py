import json

import flask
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import UserSchema
from .service import Userservice
from .model import User
from .interface import UserInterface
from flask import jsonify
from datetime import datetime

api = Namespace("User", description="A modular namespace within user")  # noqa


@api.route("/")
class UserResource(Resource):

    def get(self) -> List[User]:
        """Get all User"""
        # search by first_name and last_name
        args = request.args
        filters = list()
        if "first_name" in args:
            filters.append({'model': 'Widget', 'field': 'first_name', 'op': '==', 'value': args["first_name"]})
        if "last_name" in args:
            filters.append({'model': 'Widget', 'field': 'last_name', 'op': '==', 'value': args["last_name"]})
            return Userservice.get_all(filters)
    #    args = request.args
    #    if "first_name" in args:
    #       first_name = args["first_name"]
    #       return Userservice.get_by_name(first_name)

    #    all_user = Userservice.get_all()
    #    print(all_user[0].user_id)
       # resp.headers["Total_length"] = len (all_user)
       # resp.data = (json.dumps(all_user))
    #    return all_user

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        obj = request.parsed_obj
        obj["full_name"] = obj["first_name"] +" "+ obj["last_name"]
        obj["created_at"] = datetime.now()
        resp = Response(status=201)
        min = int(request.headers["min-length"])
        print(f"min length{min}")

        if len(obj["first_name"]) < min:
            return Response(status=400, response="letter must be greater than {min}")
        use1 = Userservice.create(obj)
        resp.headers["user_id"] = use1.user_id
        return resp

    @api.route("/<int:user_id>")
    @api.param("user_id", "user database ID")
    class UseridResource(Resource):
        @responds(schema=UserSchema)
        def get(self, user_id: int) -> User:
            id = Userservice.get_by_id(user_id)

            if id:
                return id
            else:
                return Response(status=404, response="Id Not EXist")

        def delete(self, user_id: int) -> Response:
            id = Userservice.delete_by_id(user_id)
            if id:
                 return jsonify(dict(status="Success", id=id))
            else:
                return Response(status=404, response="Id Not EXist")

        @accepts(schema=UserSchema, api=api)
        @responds(schema=UserSchema)
        def patch(self, user_id: int) ->User:

            changes: UserInterface = request.parsed_obj
            User = Userservice.get_by_id(user_id)
            return Userservice.update(User, changes)


