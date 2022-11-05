import sqlalchemy as sa

from database.db import Base


class Questions(Base):
    __tablename__ = 'questions'
    id = sa.Column(sa.Integer, primary_key=True)
    answer = sa.Column(sa.Text)
    question = sa.Column(sa.Text)

    def __repr__(self):
        return f"Questions(id={self.id!r}, question={self.question!r}, answer={self.answer!r})"