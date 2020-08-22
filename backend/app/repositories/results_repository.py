from typing import List

from .base import session_maker
from app.models import Result


class ResultRepository:
    def __init__(self):
        self.session = session_maker()

    def all(self) -> List[Result]:
        results = self.session.query(Result).all()
        self.session.rollback()
        return results

    def create(self, model: Result) -> Result:
        self.session.add(model)
        self.session.commit()

        return model

    def update(self, model: Result) -> Result:
        self.session.add(model)
        self.session.commit()

        return model
