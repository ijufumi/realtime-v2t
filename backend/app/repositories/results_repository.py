from typing import List, Optional

from .base import session_maker
from app.models import Result


class ResultRepository:
    def __init__(self):
        self.session = session_maker()

    def all(self) -> List[Result]:
        results = self.session.query(Result).all()
        self.session.rollback()
        return results

    def find_by_id(self, id: str) -> Optional[Result]:
        result = self.session.query(Result).filter(Result.id == id).first()
        self.session.rollback()
        return result

    def create(self, model: Result) -> Result:
        self.session.add(model)
        self.session.commit()

        return model

    def update(self, model: Result) -> Result:
        self.session.add(model)
        self.session.commit()

        return model

    def delete(self, model: Result) -> None:
        self.session.delete(model)
        self.session.commit()
