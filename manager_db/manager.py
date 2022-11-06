from sqlalchemy import select, func, insert

from database.db import session
from database.tables import Questions


class SQLManager:

    @staticmethod
    def get_question():
        stmt = select(Questions.question, Questions.answer).order_by(func.random())
        return session.execute(stmt).first()

    @staticmethod
    def get_current_question(question: str):
        stmt = select(Questions.answer).where(Questions.question==question)
        return session.execute(stmt).first()

    @staticmethod
    def create_question(question, answer):
        session.add(Questions(question=question, answer=answer))
        session.commit()