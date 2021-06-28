from mypy_extensions import TypedDict
from click import DateTime


class UserInterface(TypedDict, total=False):
    user_id: int
    first_name: str
    full_name: str
    salary: int
    created_at: DateTime

