from . import session_maker
from app.models import Result


class ResultRepository:
    def __init__(self):
        self.session = session_maker()

    def create(self, model: Result) -> Result:
        self.session.add(model)
        self.session.commit()

        return model

