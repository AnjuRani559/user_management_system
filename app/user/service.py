from app import db
from typing import List
from .model import User
from .interface import UserInterface
from sqlalchemy_filters import apply_filters


class Userservice():
    class UserService:
        @staticmethod
        def get_all(filters) -> List[User]:
            f_query = db.session.query(User)
            # add filters from list of filter
            if len(filters) > 0:
                f_query = apply_filters(f_query, filters)
                return f_query.all()

    @staticmethod
    def get_all(self)->[User]:
        return User.query.all()


    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(
        first_name=new_attrs["first_name"], last_name=new_attrs["last_name"], full_name=new_attrs["full_name"], created_at=new_attrs["created_at"], salary=  new_attrs["salary"])
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def update(user: User, User_change_updates: UserInterface) -> User:
        user.update(User_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(user_id: int) -> List[int]:
        user = User.query.filter(User.user_id == user_id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [user_id]




